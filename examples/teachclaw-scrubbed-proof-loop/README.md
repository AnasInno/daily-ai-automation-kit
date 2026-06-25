# TeachClaw Scrubbed Proof Loop

This example is a public-safe version of the operating pattern behind TeachClaw work.

It does not contain TeachClaw private source code, prompts, teacher data, pupil work, browser sessions, deployment details, Crabbox lease details, or live run logs.

It shows the loop:

```text
teacher workflow -> tight brief -> deterministic artifact plan -> validation gates -> human judgement
```

## Run

```bash
make smoke
```

This reads fake classroom input from `data/sample_teachclaw_request.json` and writes a proof packet to `output/sample_proof_packet.md`.

## Test

```bash
python3 -m pytest -q
```

## What This Proves

- the repo can turn a workflow brief into a structured proof packet
- sample mode works without secrets
- the output separates mechanical success from quality judgement
- public examples can name TeachClaw without exposing sensitive implementation details

## What This Does Not Prove

- live TeachClaw runtime behavior
- real teacher approval
- real pupil-data handling
- private prompt quality
- browser or Crabbox evidence
- Computer Use evidence
- Crabbox hydration/tool-readiness evidence
- autoreview/minimality verdict
- CI/CD verification

Those proof levels require recorded evidence and stay out of this public example.
