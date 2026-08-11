#!/usr/bin/env python3
"""Generate a blank research point canvas in Markdown."""
from pathlib import Path
import argparse

TEMPLATE = """# Research Point Canvas

## Real Demand
- task/domain:
- real scenario:
- field-recognized need:
- evidence:
- pseudo-demand risk:

## Scientific Problem
- observed bottleneck:
- underlying mechanism:
- why existing methods fail:
- problem status: well-studied / timely / emerging / not yet proposed

## Solution Method
- data-level idea:
- model-level idea:
- objective-function idea:
- learning-method idea:
- central method claim:

## Validation
- sota comparison:
- ablation:
- mechanism analysis:
- robustness/generalization:
- error analysis:

## Three-One Verdict
- one field-recognized real demand:
- one essence-hitting scientific problem:
- one effective method cutting into the problem:
"""

def main():
    parser = argparse.ArgumentParser(description='Generate a research point canvas markdown file.')
    parser.add_argument('-o', '--output', help='Output markdown file. If omitted, print to stdout.')
    args = parser.parse_args()
    if args.output:
        Path(args.output).write_text(TEMPLATE, encoding='utf-8')
        print(f'wrote {args.output}')
    else:
        print(TEMPLATE)

if __name__ == '__main__':
    main()
