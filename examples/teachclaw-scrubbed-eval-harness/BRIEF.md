# TeachClaw Scrubbed Eval Harness Brief

## One-Line Mission

Show how a TeachClaw-style workflow can evaluate output quality and routing
strategy without exposing private implementation details.

## User

An operator deciding whether an AI-assisted teaching workflow is good enough to
route by default.

## Pain

A smoke test can prove that an output exists. It cannot prove the output is
useful, safe, specific, or worth routing to a user.

## Current Workflow

The operator needs to inspect generated outputs, compare strategies, identify
weak cases, and decide whether more human review or a different strategy is
needed.

## Input

Fake public-safe JSON fixtures:

- scenario pack
- rubric
- candidate strategy scores

## Output

A machine-readable JSON scorecard and human-readable Markdown scorecard.

## Deterministic Core

The script validates fixture shape, checks rubric weights, applies fatal gates,
computes weighted scores, compares strategies, and writes scorecards.

## Optional AI Layer

Not included in this public example. In real work, an AI judge or human reviewer
can produce the dimension scores, but this example keeps fixture scoring
deterministic so it runs without secrets.

## Safety Boundaries

- no real teacher data
- no pupil work
- no private prompts
- no live model traces
- no browser/session details
- no Crabbox broker or lease metadata
- no external writes

## Smoke Test

```bash
make smoke
```

## Proof Ladder

- CLI smoke: generated JSON and Markdown scorecards
- Unit tests: validation, scoring, and failure behavior
- Sample output: public-safe fixture scorecard
- Human quality judgement: needed for real outputs
- Browser proof: not run
- Computer Use proof: not run
- Crabbox hydration/tool readiness: not run
- Crabbox proof: not run
- Autoreview/minimality verdict: not run
- CI/CD verification: repo-level PR/ship step, not part of this example
