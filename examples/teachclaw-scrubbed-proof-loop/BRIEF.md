# TeachClaw Scrubbed Workflow Brief

## One-Line Mission

Show how a real TeachClaw-style workflow moves from teacher request to artifact plan and validation gates without exposing private product details.

## User

A teacher who wants useful teaching support without more admin to inspect.

## Pain

Teacher asks for help, but the output only matters if it is grounded, useful, and checked at the right surface.

## Current Workflow

The operator needs to understand the teacher request, inspect available evidence, create a useful artifact plan, then verify whether the result is mechanically present and pedagogically good enough.

## Input

Fake classroom request JSON with:

- teacher request
- fictional class context
- fake misconceptions
- desired artifact
- forbidden actions
- required proof

## Output

A Markdown proof packet containing:

- conversation brief
- deterministic artifact plan
- validation gates
- safety boundaries
- final status

## Deterministic Core

The script validates required fields, extracts key context, builds a simple artifact plan, and assigns validation statuses.

## Optional AI Layer

Not included in this public example. In real work, AI may help with judgement, generation, summarisation, or critique, but the proof boundary remains explicit.

## Safety Boundaries

- no real teacher data
- no pupil work
- no private prompts
- no live browser/session details
- no Crabbox broker or lease metadata
- no external writes

## Smoke Test

```bash
make smoke
```

## Proof Ladder

- CLI smoke: generated `output/sample_proof_packet.md`
- Unit tests: deterministic validation and output checks
- Sample output: public-safe Markdown proof packet
- Browser proof: not run
- Computer Use proof: not run
- Crabbox hydration/tool readiness: not run
- Crabbox proof: not run
- Autoreview/minimality verdict: not run
- CI/CD verification: repo-level PR/ship step, not part of this example
- Human quality judgement: marked as needed
