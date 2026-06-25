---
name: how-i-engineer-autoreview
description: "Use after a build, orchestration pass, or merge candidate to review fit against the brief, minimality, proof claims, and public safety."
---

# Autoreview

Use this skill when an artifact needs an independent review pass before it is
called ready.

This is for:

- checking whether the output still matches the original brief
- catching scope creep and overbuilt code
- separating mechanical success from useful output
- checking that claims match recorded proof
- finding public-safety leaks before release

This is not for:

- rewriting the project from taste alone
- adding new features during review
- treating a green test run as a full quality verdict
- approving external actions

## Review Loop

1. Read the brief, changed files, README, sample inputs, and sample outputs.
2. Check the smallest useful slice: one user, one input shape, one output
   format, one smoke command, one proof standard.
3. Challenge overengineering: unused abstractions, broad integrations, extra
   services, hidden state, unnecessary dependencies, or AI where deterministic
   logic is enough.
4. Check output usefulness against the stated workflow.
5. Check proof claims against evidence: CLI, tests, eval, browser, Crabbox,
   public safety scan, or human judgement.
6. Check public safety: no secrets, private paths, live logs, customer data,
   browser sessions, inboxes, or private run details.
7. Return findings first, then a verdict.

## Minimality Gate

Every addition should earn its place by doing at least one of these:

- reduces repeated human work
- closes a real failure mode
- makes proof clearer
- makes handoff easier for the next agent or human

If it only makes the repo look more impressive, recommend removing it.

## Output Standard

Return:

- findings ordered by severity, with file references when relevant
- overengineering risks
- missing proof or overclaimed proof
- public-safety concerns
- suggested deletes or trims
- verdict: `pass`, `trim`, `needs repair`, or `needs judgement`

Do not change code during autoreview unless the user explicitly asks for fixes.
