#!/usr/bin/env python3
"""Bounded offline regressions for the real, source-preserving web artifact."""
import hashlib
import json
from pathlib import Path
import struct
import tempfile
import unittest
import zipfile

from build_release import ROOT, build, verify_archive, zip_info


class WebDistributionTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='academic-web-test-')
        self.addCleanup(self.temp.cleanup)
        self.output = Path(self.temp.name)
        self.report = build(ROOT, self.output / 'built', 'web-plugin')[0]
        self.archive = self.output / 'built' / self.report['file']
        with zipfile.ZipFile(self.archive) as z:
            self.data = {n: z.read(n) for n in z.namelist()}
        self.top = self.report['root']
        self.manifest_path = f'{self.top}/release-manifest.json'

    def write_mutation(self, data, name='mutation.zip'):
        path = self.output / name
        with zipfile.ZipFile(path, 'w') as z:
            for n, b in data.items():
                z.writestr(zip_info(n), b)
        return path

    def update_manifest(self, data):
        manifest = json.loads(data[self.manifest_path])
        for row in manifest['files']:
            content = data[f"{self.top}/{row['path']}"]
            row['size'] = len(content)
            row['sha256'] = hashlib.sha256(content).hexdigest()
        data[self.manifest_path] = json.dumps(manifest).encode()

    def test_real_payload_identity_hash_crc_and_complete_source_preservation(self):
        self.assertEqual(self.top, 'academic-research')
        self.assertEqual(self.report['kind'], 'web-plugin')
        self.assertEqual(self.report['sha256'], hashlib.sha256(self.archive.read_bytes()).hexdigest())
        expected = {'plugin.json', 'LICENSE', 'NOTICE'} | {
            p.relative_to(ROOT).as_posix() for p in (ROOT / 'skills').rglob('*')
            if p.is_file() and '__pycache__' not in p.parts
        }
        actual = {n.removeprefix(self.top + '/') for n in self.data} - {'release-manifest.json'}
        self.assertEqual(actual, expected)
        self.assertEqual(len([n for n in actual if n.startswith('skills/')]), 46)
        for n in actual:
            self.assertEqual(self.data[f'{self.top}/{n}'], (ROOT / n).read_bytes(), n)
        self.assertFalse(any('marketplace' in n or '/.github/' in n for n in self.data))
        self.assertEqual(verify_archive(self.archive, root=ROOT)['files_verified'], 49)
        with zipfile.ZipFile(self.archive) as z:
            self.assertIsNone(z.testzip())
        manifest = json.loads(self.data[f'{self.top}/plugin.json'])
        self.assertEqual(manifest['version'], json.loads((ROOT / 'package.json').read_text())['version'])
        self.assertEqual(len('academic-research:research-english-academic-paper-writing-guide'), 63)

    def test_reproducible_web_archive_and_all_includes_it(self):
        second = build(ROOT, self.output / 'second', 'web-plugin')[0]
        self.assertEqual(second['sha256'], self.report['sha256'])
        reports = build(ROOT, self.output / 'all', 'all')
        self.assertEqual({r['kind'] for r in reports}, {'skill', 'plugin', 'web-plugin'})
        self.assertEqual(next(r['sha256'] for r in reports if r['kind'] == 'web-plugin'), self.report['sha256'])

    def test_source_change_and_self_consistent_omission_rejected(self):
        data = dict(self.data)
        target = next(n for n in data if n.endswith('/references/quick-reference.md'))
        data[target] += b'\n'
        self.update_manifest(data)
        with self.assertRaisesRegex(ValueError, 'Source mismatch'):
            verify_archive(self.write_mutation(data), root=ROOT)
        data = dict(self.data)
        del data[target]
        manifest = json.loads(data[self.manifest_path])
        manifest['files'] = [r for r in manifest['files'] if f"{self.top}/{r['path']}" != target]
        data[self.manifest_path] = json.dumps(manifest).encode()
        with self.assertRaisesRegex(ValueError, 'every tracked skill file'):
            verify_archive(self.write_mutation(data, 'omitted.zip'), root=ROOT)

    def test_encoding_cannot_bypass_original_source_verification(self):
        data = dict(self.data)
        target = next(n for n in data if n.endswith('/references/quick-reference.md'))
        data[target] += b'\nAltered source.\n'
        self.update_manifest(data)
        manifest = json.loads(data[self.manifest_path])
        row = next(r for r in manifest['files'] if f"{self.top}/{r['path']}" == target)
        row['encoding'] = 'base64'
        data[self.manifest_path] = json.dumps(manifest).encode()
        with self.assertRaisesRegex(ValueError, 'original unencoded source bytes'):
            verify_archive(self.write_mutation(data), root=ROOT)

    def test_unknown_kind_cannot_bypass_web_checks(self):
        data = dict(self.data)
        manifest = json.loads(data[self.manifest_path])
        manifest['kind'] = 'unknown'
        for row in manifest['files']:
            row.pop('source_relative', None)
        data[self.manifest_path] = json.dumps(manifest).encode()
        with self.assertRaisesRegex(ValueError, 'Unsupported archive kind'):
            verify_archive(self.write_mutation(data), root=ROOT)

    def test_payload_hash_mutation_rejected(self):
        data = dict(self.data)
        data[f'{self.top}/LICENSE'] += b'\n'
        with self.assertRaisesRegex(ValueError, 'ZIP byte mismatch'):
            verify_archive(self.write_mutation(data))

    def test_manifest_identity_schema_version_and_skill_identity_rejected(self):
        for label, edit in {
            'name': lambda m: m.update(name='renamed-package'),
            'schema': lambda m: m.update({'$schema': 'unsupported'}),
            'version': lambda m: m.update(version='0.0.0'),
        }.items():
            with self.subTest(label=label):
                data = dict(self.data)
                manifest = json.loads(data[f'{self.top}/plugin.json'])
                edit(manifest)
                data[f'{self.top}/plugin.json'] = json.dumps(manifest).encode()
                self.update_manifest(data)
                with self.assertRaises(ValueError):
                    verify_archive(self.write_mutation(data, label + '.zip'))
        # A valid but overlong real skill namespace must fail independently of hashes.
        data = dict(self.data)
        new_top = 'academic-research-long'
        data = {n.replace(self.top + '/', new_top + '/', 1): b for n, b in data.items()}
        manifest_path = new_top + '/release-manifest.json'
        manifest = json.loads(data[manifest_path]); manifest['root'] = new_top
        plugin_path = new_top + '/plugin.json'
        plugin = json.loads(data[plugin_path]); plugin['name'] = new_top
        data[plugin_path] = json.dumps(plugin).encode()
        for row in manifest['files']:
            if row['path'] == 'plugin.json':
                row.update(size=len(data[plugin_path]), sha256=hashlib.sha256(data[plugin_path]).hexdigest())
        data[manifest_path] = json.dumps(manifest).encode()
        with self.assertRaisesRegex(ValueError, 'identity exceeds 64'):
            verify_archive(self.write_mutation(data, 'long.zip'))

    def test_unsafe_extra_duplicate_paths_rejected(self):
        for path in [f'{self.top}/../escape', f'{self.top}//double', f'{self.top}/./dot', f'{self.top}/bad\\name']:
            with self.subTest(path=path):
                data = dict(self.data); data[path] = b'x'
                with self.assertRaises(ValueError):
                    verify_archive(self.write_mutation(data))
        path = self.write_mutation(self.data, 'duplicate.zip')
        import warnings
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', UserWarning)
            with zipfile.ZipFile(path, 'a') as z:
                z.writestr(zip_info(self.manifest_path), self.data[self.manifest_path])
        with self.assertRaisesRegex(ValueError, 'Duplicate ZIP names'):
            verify_archive(path)

    def test_crc_corruption_rejected(self):
        raw = bytearray(self.archive.read_bytes())
        with zipfile.ZipFile(self.archive) as z:
            info = z.getinfo(f'{self.top}/LICENSE')
        offset = info.header_offset
        name_len, extra_len = struct.unpack_from('<HH', raw, offset + 26)
        payload = offset + 30 + name_len + extra_len
        raw[payload + info.compress_size // 2] ^= 1
        path = self.output / 'crc.zip'; path.write_bytes(raw)
        import zlib
        with self.assertRaises((zipfile.BadZipFile, zlib.error, ValueError)):
            verify_archive(path)



class OfflineClosureTest(unittest.TestCase):
    """Exercise extracted artifacts, never a source checkout as runtime fallback."""
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(prefix='academic-offline-closure-')
        cls.directory = Path(cls.temp.name)
        cls.reports = build(ROOT, cls.directory / 'artifacts', 'all')
        baseline = json.loads((ROOT / 'docs/distribution-baseline.json').read_text())
        cls.course = [r for r in baseline['files']
                      if r['path'] == 'docs/course-full-reconstruction.md'
                      or r['path'].endswith('/references/course-full-reconstruction.md')
                      or '/references/lectures/' in r['path']]
        assert len(cls.course) == 15

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def extract(self, kind, name):
        report = next(r for r in self.reports if r['kind'] == kind)
        destination = self.directory / name
        with zipfile.ZipFile(self.directory / 'artifacts' / report['file']) as archive:
            archive.extractall(destination)
        top = destination / report['root']
        skill = top if kind == 'skill' else top / 'skills/research-english-academic-paper-writing-guide'
        return top, skill

    def assert_closure(self, top, skill):
        # Manifest is checked against extracted bytes, not ROOT or a downloaded file.
        manifest = json.loads((top / 'release-manifest.json').read_text())
        for row in manifest['files']:
            content = (top / row['path']).read_bytes()
            self.assertEqual(len(content), row['size'])
            self.assertEqual(hashlib.sha256(content).hexdigest(), row['sha256'])
        for relative in ['SKILL.md', 'references/installation.md',
                         'references/course-review-notes.md',
                         'references/course-full-reconstruction.md',
                         'references/lecture-index.md', 'references/provenance.md',
                         'references/quick-reference.md']:
            self.assertTrue((skill / relative).is_file(), relative)
        self.assertEqual(len(list((skill / 'references/lectures').glob('*.md'))), 13)
        self.assertEqual(len(list((skill / 'references/playbooks').glob('*.md'))), 19)
        # Both baseline full-course copies have the same digest; each has a local
        # complete representative. Unique course bytes may never be omitted.
        for row in self.course:
            relative = ('references/course-full-reconstruction.md'
                        if row['path'].startswith('docs/') else
                        row['path'].removeprefix('skills/research-english-academic-paper-writing-guide/'))
            self.assertEqual(hashlib.sha256((skill / relative).read_bytes()).hexdigest(), row['sha256'])
        guide = (skill / 'references/installation.md').read_text()
        self.assertNotRegex(guide, r'https?://|git clone|npx --|npm install|git checkout')
        self.assertIn('Windows', guide)
        self.assertIn('Linux', guide)
        self.assertIn('当前取得的仓库、发布包及工作目录没有可交付', guide)
        self.assertIn('尚不能据此认定完成', guide)
        self.assertIn('不以联网链接或转写替代原件', guide)
        self.assertIn('正常离线带读', guide)
        self.assertNotIn('请使用 [已发布v4.7.4]', guide)
        notice = (skill / 'SKILL.md').read_text().split('# Research and English Academic Paper Writing Guide\n', 1)[0]
        self.assertIn('Original PDF/transcript', notice)
        self.assertIn('local delivery of', notice)
        self.assertIn('not complete', notice)
        self.assertIn('references/installation.md', notice)

    def test_three_artifacts_are_closed_and_all_course_bytes_preserved(self):
        for kind in ['skill', 'plugin', 'web-plugin']:
            with self.subTest(kind=kind):
                top, skill = self.extract(kind, 'complete-' + kind)
                self.assert_closure(top, skill)
                self.assertFalse(any(top.rglob('.git')))
                self.assertFalse(any(top.rglob('*.pdf')))
                self.assertFalse(any(top.rglob('*.transcript.txt')))
                if kind == 'plugin':
                    self.assertTrue((top / 'plugin.json').is_file())
                    self.assertTrue((top / '.claude-plugin/plugin.json').is_file())
                    self.assertTrue((top / 'bin/install.mjs').is_file())
                elif kind == 'web-plugin':
                    self.assertFalse((top / 'bin').exists())
                    self.assertFalse((top / 'docs').exists())

    def test_helpers_execute_from_isolated_extraction_with_network_blocked(self):
        import subprocess
        import sys
        top, skill = self.extract('web-plugin', 'script-runtime')
        for script, arguments in [('check_title.py', ['A Study of Visual Question Answering']),
                                  ('new_research_point_canvas.py', []),
                                  ('measure_prose_rhythm.py', ['--help'])]:
            relative = 'scripts/' + script
            self.assertTrue((skill / relative).is_file())
            # -I removes user/site path injection; cwd is the extraction, and
            # fail-closed Python network hooks prevent helpers using the network.
            driver = ('import runpy,socket,sys; '
                      'exec("def blocked(*a, **k): raise RuntimeError(\\"Network forbidden\\")"); '
                      'socket.socket=blocked; socket.create_connection=blocked; '
                      'sys.argv=' + repr([relative] + arguments) + '; '
                      'runpy.run_path(' + repr(relative) + ',run_name="__main__")')
            result = subprocess.run([sys.executable, '-I', '-c', driver], cwd=skill,
                                    capture_output=True, text=True, timeout=15)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue(result.stdout.strip())

    def test_missing_guide_course_and_remote_dependency_are_rejected(self):
        for label, relative in [('guide', 'references/installation.md'),
                                ('course', 'references/course-full-reconstruction.md')]:
            top, skill = self.extract('web-plugin', 'missing-' + label)
            (skill / relative).unlink()
            with self.assertRaises((AssertionError, FileNotFoundError)):
                self.assert_closure(top, skill)
        top, skill = self.extract('web-plugin', 'remote-dependency')
        guide = skill / 'references/installation.md'
        guide.write_text(guide.read_text() + '\nRequired: https://example.invalid/WEB-PLUGIN.md\n')
        # Reconcile the integrity manifest to prove semantic closure catches the
        # dependency even when file hashes are internally consistent.
        manifest_path = top / 'release-manifest.json'
        manifest = json.loads(manifest_path.read_text())
        row = next(r for r in manifest['files'] if r['path'].endswith('/references/installation.md'))
        row.update(size=guide.stat().st_size, sha256=hashlib.sha256(guide.read_bytes()).hexdigest())
        manifest_path.write_text(json.dumps(manifest))
        with self.assertRaises(AssertionError):
            self.assert_closure(top, skill)


if __name__ == '__main__':
    unittest.main()
