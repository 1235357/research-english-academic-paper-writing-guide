#!/usr/bin/env python3
"""Bounded regressions for operational guidance, not a full source-fidelity proof."""
from pathlib import Path
import types
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills/research-english-academic-paper-writing-guide'
PLAYBOOKS = SKILL / 'references/playbooks'

def read(path):
    return path.read_text(encoding='utf-8')

def normalized(path):
    return ' '.join(read(path).split())

def require_detector_noninference(text):
    text = ' '.join(text.split())
    for forbidden in (
        'CV alone does not explain a change of that size',
        'rate on the same *kind* of bias moving by an order of magnitude',
        'one benchmark and another over eighteen months',
    ):
        if forbidden in text.replace('**', ''):
            raise AssertionError('Unsupported detector inference: ' + forbidden)
    for required in (
        'do not establish whether CV contributed to the reported score change',
        'do not establish a longitudinal change in a directly comparable false-positive rate',
    ):
        if required not in text:
            raise AssertionError('Missing non-inference boundary: ' + required)


def require_course_review_contract(skill):
    """Static conflict guards, not a claim to simulate model behavior."""
    notes = normalized(skill / 'references/course-review-notes.md')
    router = normalized(skill / 'SKILL.md')
    requirements = (
        'these named corrections take precedence',
        'SOTA and ablations are not mandatory',
        'Method-first exploration and transfer are legitimate starts',
        'Do not infer independence/seniority',
        'Separate observation, candidate explanation and independently tested mechanism',
        'not a verified primary study or ML mechanism proof',
        'Never invent prior-method failure or proposed success',
        'document-only knowledge, not completed inspection',
        'Linked Method text may supply indispensable implementation/reproduction detail',
    )
    for phrase in requirements:
        if phrase not in notes:
            raise AssertionError('Missing course correction: ' + phrase)
    if 'references/course-review-notes.md' not in router or 'override conflicting archived instructions' not in router:
        raise AssertionError('Current-review precedence is not routed')
    forbidden = {
        '11-innovation-angles.md': ('Require SOTA comparison, ablation, and at least one mechanism-oriented analysis',
                                   'which is the mechanism-level reason', 'recalls significantly more accurately'),
        '01-overview.md': ('probably operating at the late stage', 'each capped by a CCF-A paper'),
        '09-concise-and-rigorous.md': ('into three single-purpose sentences', '44-word, comma-chained sentence'),
        '14-figure-schema-and-rendering-gate.md': ('never to lengthen the caption', "The figure's job is everything else", 'the figure IS the method'),
        '12-find-papers-literature-review.md': ('Prioritize papers that meet most',),
    }
    for name, phrases in forbidden.items():
        content = normalized(skill / 'references/playbooks' / name)
        for phrase in phrases:
            if phrase in content:
                raise AssertionError('Conflicting active rule: ' + name + ': ' + phrase)


class SemanticCoherence(unittest.TestCase):
    def test_full_course_review_contract(self):
        require_course_review_contract(SKILL)
        self.assertIn('observed versus schematic status', normalized(PLAYBOOKS / '06-motivation-figure.md'))
        self.assertIn('document-only knowledge', normalized(PLAYBOOKS / '12-find-papers-literature-review.md'))
        self.assertIn('MuKEA (motivation V1→V4, framework V1→V8)', normalized(SKILL / 'SKILL.md'))
        self.assertIn('ET-BERT (motivation V1→V3, framework V1→V4', normalized(SKILL / 'SKILL.md'))

    def test_course_correction_mutations_are_rejected(self):
        # Work only in isolated fixtures; never mutate the checked package.
        import shutil
        import tempfile
        with tempfile.TemporaryDirectory(prefix='course-contract-') as temp:
            fixture = Path(temp) / 'skill'
            shutil.copytree(SKILL, fixture, ignore=shutil.ignore_patterns('__pycache__'))
            notes = fixture / 'references/course-review-notes.md'
            original = read(notes)
            notes.write_text(original.replace('these named corrections take precedence', 'the archive always wins'))
            with self.assertRaisesRegex(AssertionError, 'Missing course correction'):
                require_course_review_contract(fixture)
            notes.write_text(original)
            for name, mutation in (
                ('11-innovation-angles.md', 'Require SOTA comparison, ablation, and at least one mechanism-oriented analysis'),
                ('01-overview.md', 'probably operating at the late stage'),
                ('09-concise-and-rigorous.md', 'into three single-purpose sentences'),
                ('14-figure-schema-and-rendering-gate.md', 'never to lengthen the caption'),
                ('12-find-papers-literature-review.md', 'Prioritize papers that meet most'),
            ):
                path = fixture / 'references/playbooks' / name
                before = read(path)
                path.write_text(before + '\n' + mutation + '\n')
                with self.subTest(file=name), self.assertRaisesRegex(AssertionError, 'Conflicting active rule'):
                    require_course_review_contract(fixture)
                path.write_text(before)

    def test_limitation_placement_does_not_hide_critical_boundaries(self):
        for name in ('13-review-feedback-evidence-contract.md', '18-submission-sprint-discipline.md'):
            text = normalized(PLAYBOOKS / name)
            self.assertNotIn('state it exactly once', text)
            self.assertNotIn('State each limitation **once**', text)
            self.assertNotIn('generally the supplement', text)
            self.assertIn('conclusion', text)
        title = 'Limitation honesty, placement, and conclusion closure'
        self.assertIn('### ' + title, read(PLAYBOOKS / '05-experiments-conclusion-references.md'))
        self.assertIn(title, read(PLAYBOOKS / '13-review-feedback-evidence-contract.md'))
        self.assertIn(title, read(PLAYBOOKS / '18-submission-sprint-discipline.md'))

    def test_rendering_requires_specific_request_but_can_be_delegated(self):
        text = normalized(PLAYBOOKS / '14-figure-schema-and-rendering-gate.md')
        self.assertIn('explicit, per-figure request', text)
        self.assertIn('author or an agent explicitly asked to render', text)
        self.assertNotIn('(not the agent)', text)
        self.assertNotIn('An agent may not render the final artwork.', text)
        self.assertIn('evidence, visual QA, attribution, and venue-policy checks', text)
        self.assertIn('without an explicit, per-figure request', normalized(SKILL / 'SKILL.md'))

    def test_rhythm_is_not_a_detector_proxy(self):
        text = normalized(PLAYBOOKS / '17-native-register-and-ai-detection.md')
        self.assertIn('Length variation is not surprisal variation.', text)
        self.assertIn('n = 1', text)
        self.assertIn('not a clean test of false positives on wholly human text', text)
        for unsupported in ('Every one of them also moves text', 'raises both CV and',
                            'same benchmark eighteen months apart', 'Lexical and syntactic unpredictability almost certainly'):
            self.assertNotIn(unsupported, text)
        self.assertIn('do not imply a particular sentence-length distribution', text)

    def test_detector_comparisons_do_not_infer_causes_or_time_series(self):
        require_detector_noninference(read(PLAYBOOKS / '17-native-register-and-ai-detection.md'))

    def test_surviving_detector_inference_mutations_are_rejected(self):
        text = read(PLAYBOOKS / '17-native-register-and-ai-detection.md')
        mutations = (
            '**CV\n alone does not explain a change of that size.**',
            "The false-positive rate on the same *kind* of bias moving by an\n order of magnitude between one benchmark and another over eighteen months.",
        )
        for mutation in mutations:
            with self.subTest(mutation=mutation):
                with self.assertRaisesRegex(AssertionError, 'Unsupported detector inference'):
                    require_detector_noninference(text + '\n' + mutation)

    def test_short_claims_remain_in_rhythm_population(self):
        path = SKILL / 'scripts/measure_prose_rhythm.py'
        # Execute source without importlib's bytecode cache: npm packages the
        # Skill directory, so tests must not add runtime artifacts to it.
        module = types.ModuleType('rhythm')
        exec(compile(read(path), str(path), 'exec'), module.__dict__)
        self.assertEqual(module.sentences('Transfer is weak. This longer sentence gives its supporting detail.'),
                         ['Transfer is weak.', 'This longer sentence gives its supporting detail.'])
        self.assertEqual(module.sentences('No. Why? This works.'), ['No.', 'Why?', 'This works.'])
        self.assertEqual(module.sentences(''), [])
        self.assertEqual(len(module.sentences('Fig. 2 shows the output. It is weak.')), 2)
        self.assertIn('Transfer is weak.', module.strip_latex(r'\section{Results} Transfer is weak.'))

    def test_peer_review_claim_includes_quality_control(self):
        text = normalized(PLAYBOOKS / '16-fast-reader-and-skim-path.md')
        self.assertIn('after controlling for paper quality', text)
        self.assertIn('https://arxiv.org/abs/2601.20920', text)
        self.assertIn('not genuine preference', text)

    def test_source_format_exclusion_is_not_content_exclusion(self):
        self.assertIn('verbatim transcript appendices', normalized(ROOT / 'NOTICE'))
        self.assertIn('Verbatim transcript text is present', normalized(SKILL / 'references/provenance.md'))
        self.assertIn('Markdown 讲义含逐字转写附录', normalized(ROOT / 'README.md'))
        self.assertNotIn('raw transcripts are **not redistributed**', read(SKILL / 'references/provenance.md'))

    def test_page_count_correction_has_date_and_primary_source(self):
        text = normalized(SKILL / 'SKILL.md')
        self.assertIn('Editorial correction (2026-10-13)', text)
        self.assertIn('has 28 pages in the version checked', text)
        self.assertIn('https://mathvault.ca/wp-content/uploads/Comprehensive-List-of-Mathematical-Symbols.pdf', text)

if __name__ == '__main__':
    unittest.main()
