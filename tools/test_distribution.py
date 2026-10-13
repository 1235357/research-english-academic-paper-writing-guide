#!/usr/bin/env python3
"""Regression: OpenAI plugin:skill identity limits are separate from npm names.

Requirement: https://developers.openai.com/plugins/deploy/submission-errors
"""
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from validate_distribution import ROOT, check


class PluginIdentityTest(unittest.TestCase):
    def test_plugin_identity_boundaries_without_renaming_skill_or_npm(self):
        with tempfile.TemporaryDirectory(prefix="research-distribution-") as temporary:
            root = Path(temporary) / "repository"
            shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns('.git', '__pycache__'))
            original_package = (root / 'package.json').read_bytes()
            skill = 'research-english-academic-paper-writing-guide'
            for length, passes in [(17, True), (18, True), (19, False), (45, False)]:
                with self.subTest(combined_length=length + 1 + len(skill)):
                    plugin_name = 'a' * length
                    for relative in ['plugin.json', '.claude-plugin/plugin.json']:
                        path = root / relative
                        manifest = json.loads(path.read_text())
                        manifest['name'] = plugin_name
                        path.write_text(json.dumps(manifest))
                    for relative in ['.agents/plugins/marketplace.json', '.claude-plugin/marketplace.json']:
                        path = root / relative
                        manifest = json.loads(path.read_text())
                        manifest['plugins'][0]['name'] = plugin_name
                        path.write_text(json.dumps(manifest))
                    report = check(root)
                    self.assertEqual(report['passed'], passes, report['errors'])
                    identity_errors = [e for e in report['errors'] if 'skill_identity_too_long' in e]
                    self.assertEqual(bool(identity_errors), not passes)
                    self.assertEqual((root / 'package.json').read_bytes(), original_package)
                    self.assertEqual(report['skill_names'], [skill])

    def test_directory_label_boundary(self):
        with tempfile.TemporaryDirectory(prefix="research-labels-") as temporary:
            root = Path(temporary) / "repository"
            shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns('.git', '__pycache__'))
            path = root / 'plugin.json'
            original = json.loads(path.read_text())
            for field in ['displayName', 'shortDescription']:
                for length, passes in [(30, True), (31, False)]:
                    with self.subTest(field=field, length=length):
                        manifest = json.loads(json.dumps(original))
                        manifest['extensions']['com.openai']['interface'][field] = 'a' * length
                        path.write_text(json.dumps(manifest))
                        report = check(root)
                        self.assertEqual(report['passed'], passes, report['errors'])
                        self.assertEqual(any(field in e for e in report['errors']), not passes)


class SemanticAmendmentTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="research-amendments-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "repository"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('.git', '__pycache__'))

    def test_exact_derived_amendments_pass_and_original_baseline_unchanged(self):
        self.assertEqual((self.root / 'docs/distribution-baseline.json').read_bytes(),
                         (ROOT / 'docs/distribution-baseline.json').read_bytes())
        report = check(self.root)
        self.assertTrue(report['passed'], report['errors'])
        self.assertEqual(len(report['derived_files_with_explicit_amendments']), 24)
        self.assertFalse(any('/lectures/' in p for p in report['derived_files_with_explicit_amendments']))

    def test_all_fifteen_course_originals_are_exact_and_reject_changes(self):
        import hashlib
        from validate_distribution import course_original
        baseline = json.loads((self.root / 'docs/distribution-baseline.json').read_text())
        originals = [row for row in baseline['files'] if course_original(row['path'])]
        self.assertEqual(len(originals), 15)
        for row in originals:
            with self.subTest(path=row['path']):
                path = self.root / row['path']
                before = path.read_bytes()
                self.assertEqual(len(before), row['size'])
                self.assertEqual(hashlib.sha256(before).hexdigest(), row['sha256'])
                path.write_bytes(before + b'\nUnreviewed source alteration.\n')
                report = check(self.root)
                self.assertFalse(report['passed'])
                self.assertIn('Course original must remain byte-identical: ' + row['path'], report['errors'])
                path.write_bytes(before)

    def test_added_review_layer_bytes_scope_and_metadata_are_checked(self):
        manifest_path = self.root / 'docs/semantic-amendments.json'
        original = json.loads(manifest_path.read_text())
        self.assertEqual(len(original['added_files']), 1)
        row = original['added_files'][0]
        note = self.root / row['path']
        before = note.read_bytes()
        note.write_bytes(before + b'\nUnreviewed change.\n')
        self.assertIn('Added bytes differ from exact reviewed replacement: ' + row['path'], check(self.root)['errors'])
        note.write_bytes(before)
        mutations = {
            'hash': lambda m: m['added_files'][0].update(after_sha256='0' * 64),
            'size': lambda m: m['added_files'][0].update(after_size=1),
            'reason': lambda m: m['added_files'][0].update(reason=''),
            'source_path': lambda m: m['added_files'][0].update(path='docs/course-full-reconstruction.md'),
            'escape': lambda m: m['added_files'][0].update(path='../not-permitted'),
            'missing': lambda m: m.update(added_files=[]),
            'duplicate': lambda m: m['added_files'].append(m['added_files'][0]),
        }
        for name, mutate in mutations.items():
            with self.subTest(mutation=name):
                manifest = json.loads(json.dumps(original))
                mutate(manifest)
                manifest_path.write_text(json.dumps(manifest))
                self.assertFalse(check(self.root)['passed'])
        manifest_path.write_text(json.dumps(original))
        report = check(self.root)
        self.assertTrue(report['passed'], report['errors'])
        self.assertEqual(report['added_files_with_explicit_review'], [row['path']])

    def test_unreviewed_derived_bytes_rejected(self):
        path = self.root / 'NOTICE'
        path.write_text(path.read_text() + '\nUnreviewed change.\n')
        report = check(self.root)
        self.assertFalse(report['passed'])
        self.assertTrue(any('exact reviewed replacement: NOTICE' in e for e in report['errors']))

    def test_every_amended_payload_rejects_unreviewed_bytes(self):
        manifest = json.loads((self.root / 'docs/semantic-amendments.json').read_text())
        self.assertEqual(len(manifest['files']), 24)
        for row in manifest['files']:
            with self.subTest(path=row['path']):
                path = self.root / row['path']
                before = path.read_bytes()
                path.write_bytes(before + b'\nUnreviewed derived change.\n')
                report = check(self.root)
                self.assertFalse(report['passed'])
                self.assertIn('Amended bytes differ from exact reviewed replacement: ' + row['path'], report['errors'])
                path.write_bytes(before)

    def test_course_append_is_rejected(self):
        path = next((self.root / 'skills/research-english-academic-paper-writing-guide/references/lectures').glob('*.md'))
        path.write_text(path.read_text() + '\nUnreviewed lecture addition.\n')
        report = check(self.root)
        self.assertFalse(report['passed'])
        self.assertTrue(any('Course original must remain byte-identical' in e for e in report['errors']))

    def test_amendment_scope_hash_and_reason_mutations_rejected(self):
        path = self.root / 'docs/semantic-amendments.json'
        original = json.loads(path.read_text())
        mutations = {
            'extra_course_path': lambda m: m['files'].append({**m['files'][0], 'path': 'docs/course-full-reconstruction.md'}),
            'old_hash': lambda m: m['files'][0].update(baseline_sha256='0' * 64),
            'new_hash': lambda m: m['files'][0].update(after_sha256='0' * 64),
            'reason': lambda m: m['files'][0].update(reason=''),
            'missing_path': lambda m: m['files'].pop(),
            'duplicate_path': lambda m: m['files'].append(m['files'][0]),
        }
        for name, mutate in mutations.items():
            with self.subTest(mutation=name):
                manifest = json.loads(json.dumps(original))
                mutate(manifest)
                path.write_text(json.dumps(manifest))
                report = check(self.root)
                self.assertFalse(report['passed'], name)

    def test_before_commit_and_every_before_hash_are_pinned(self):
        path = self.root / 'docs/semantic-amendments.json'
        original = json.loads(path.read_text())
        manifest = json.loads(json.dumps(original))
        manifest['before_commit'] = '0' * 40
        path.write_text(json.dumps(manifest))
        report = check(self.root)
        self.assertFalse(report['passed'])
        self.assertIn('Amendment before commit differs from pinned snapshot', report['errors'])
        for index, row in enumerate(original['files']):
            with self.subTest(path=row['path']):
                manifest = json.loads(json.dumps(original))
                manifest['files'][index]['before_sha256'] = '0' * 64
                path.write_text(json.dumps(manifest))
                report = check(self.root)
                self.assertFalse(report['passed'])
                self.assertIn('Amendment before hash differs from pinned snapshot: ' + row['path'], report['errors'])


if __name__ == '__main__':
    unittest.main()
