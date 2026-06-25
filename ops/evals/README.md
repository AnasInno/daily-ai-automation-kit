# Eval Contracts

Use this contract for public-safe eval harnesses.

## Required Files

For a runnable eval example, prefer:

```text
examples/<slug>/
  README.md
  BRIEF.md
  VERIFY.md
  Makefile
  data/
    scenarios.json
    rubric.json
    candidate_runs.json
  output/
    scorecard.json
    scorecard.md
  scripts/
    run_eval.py
  tests/
```

## Required Fields

Every scorecard should include:

- `eval_version`
- `run_id`
- `pack_id`
- `rubric_version`
- `validation_source_of_truth`
- `mechanical_result`
- `quality_result`
- `overall_status`
- `strategy_summaries`
- `scenario_results`
- `non_claims`

## Status Rules

- `fail`: the runner broke, required data is missing, or a fatal safety gate failed
- `needs_repair`: the output is mechanically present but below merge threshold
- `needs_judgement`: fixture or automated evidence is green, but a human-quality or live proof layer is still required
- `merge_candidate`: the proof required for this public artifact has passed

Fixture-only evals may be `merge_candidate` for eval mechanics. They must not
claim live model quality, real-user approval, or production runtime behavior.

## Dimension Rules

- Use a 1 to 5 scale unless the example explains otherwise.
- Weights must sum to 1.0.
- Fatal gates override weighted averages.
- Scores should be reported per scenario and by strategy.
- Pairwise winners should be visible.

## Public Safety

Public eval fixtures must not contain real customer data, private prompts,
private model traces, browser sessions, hidden run logs, local paths, provider
tokens, or live runtime metadata.
