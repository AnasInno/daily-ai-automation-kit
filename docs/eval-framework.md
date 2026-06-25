# Eval Framework

This repo treats evals as an engineering control surface, not a dashboard garnish.

The pattern comes from TeachClaw-shaped work: outputs are only valuable when they
change the user's next action, stay inside safety boundaries, and remain reliable
enough to route by default.

## What An Eval Must Answer

An eval should answer a specific decision:

- is this workflow ready to use?
- did the new behavior improve the output in the intended direction?
- which strategy should handle this task family?
- where is a cheaper model good enough?
- where does premium judgement actually matter?
- what should be escalated to a human?

If the eval does not change a decision, it is probably just reporting.

## The Public-Safe Shape

The public harness uses fake fixtures, but keeps the real structure:

```text
scenario pack -> candidate outputs -> rubric -> deterministic scorer -> scorecard -> merge judgement
```

The private version may use live model outputs, private traces, browser proof,
Crabbox proof, teacher review, or production-like runtime evidence. This public
repo deliberately keeps those out.

## Scenario Packs

A scenario pack should include:

- `gold` cases that represent the main workflow
- `edge` cases that expose ambiguity or partial input
- `failure` cases that should force caution, fallback, or human review

Each scenario names:

- task family
- user request
- expected useful output
- risk focus
- forbidden actions
- proof needed

## Rubric Dimensions

Rubrics should be weighted and readable. Useful dimensions include:

- task completion
- evidence alignment
- teacher or operator utility
- structure compliance
- tone and specificity
- safety boundary handling
- fallback honesty

Some dimensions can be fatal gates. A high average should not hide a safety
failure.

## Strategy Comparison

Compare strategies, not just models:

- single-pass draft
- draft plus deterministic checker
- draft plus targeted repair
- cheap construction plus premium judgement
- human-review queue for high-risk cases

The best strategy is the one that produces the best user outcome at the right
cost, latency, and risk level for that task family.

## Proof Labels

Use exact proof labels:

- `fixture-rubric`
- `deterministic-scorer`
- `local-cli`
- `unit-tests`
- `sample-output`
- `browser-recorded`
- `computer-recorded`
- `tool-readiness`
- `crabbox-recorded`
- `human-output-review`
- `ci-cd-check`
- `live-runtime`

Do not flatten these into "tested".

## What Done Means

For behavior-shaping work, passing tests is not enough.

Done means:

1. the plumbing works
2. the output changes in the intended direction
3. the change fits the real workflow
4. the fallback behavior is safe
5. the proof source is explicit
6. public claims stay inside recorded evidence

The runnable public example is `examples/teachclaw-scrubbed-eval-harness/`.
