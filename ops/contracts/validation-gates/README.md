# Validation Gates

Use these gates consistently when judging a workflow.

## Gates

1. `local code validated`
Focused commands, import checks, or tests prove the touched code path.

2. `workflow mechanically validated`
The sample input actually produced the expected output file or rendered result.

3. `output quality validated`
The output is useful for the stated user workflow, not merely present.

4. `pr/ship safety validated`
The public artifact passed safety checks and does not leak private details.

5. `eval mechanics validated`
When output quality, routing, or behavior change is part of the claim, a scenario
pack, rubric, scorecard, and source-of-truth label exist.

6. `minimality validated`
An independent review confirms that the artifact still matches the brief and has
not grown into unnecessary abstractions, integrations, dependencies, or AI calls.

## Result Fields

- `mechanical_result`: `pass` or `fail`
- `quality_result`: `pass`, `fail`, or `needs_judgement`
- `validation_source_of_truth`: explicit proof source
- `minimality_result`: `pass`, `trim`, or `needs_repair`
- `overall_status`: `fail`, `needs repair`, `needs judgement`, or `merge candidate`

## Source Of Truth Values

Use the most specific value that applies:

- `local-cli`
- `unit-tests`
- `sample-output`
- `fixture-rubric`
- `deterministic-scorer`
- `browser-recorded`
- `computer-recorded`
- `tool-readiness`
- `crabbox-recorded`
- `human-output-review`
- `public-safety-scan`
- `ci-cd-check`
- `autoreview`

If a run does not say where the evidence came from, do not trust the claim.

Mechanically green but quality not judged means the status remains `needs_judgement`.
