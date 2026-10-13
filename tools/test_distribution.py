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


if __name__ == '__main__':
    unittest.main()
