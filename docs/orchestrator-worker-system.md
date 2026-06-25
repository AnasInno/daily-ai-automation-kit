# Orchestrator / Worker System

This repo uses "agentic" in the engineering sense: break ambiguous work into bounded lanes, run them with evidence, and merge only what survives verification.

For runnable procedure, use `.agents/skills/how-i-engineer-orchestrator/SKILL.md`. This document explains the model; the skill carries the operating loop.

## Before The Orchestrator

The first phase is a conversation, not a worker launch.

Use the conversation to pin down:

- the user
- the manual workflow
- the available input
- the output that changes the next action
- the risks and non-goals
- the proof that would make the result believable

Once those answers are clear, the orchestrator can manage worker threads without turning the project into a sprawling prompt.

If those answers are not clear, use `.agents/skills/how-i-engineer-conversation-brief/SKILL.md` first.

## Orchestrator

The orchestrator is responsible for judgement.

It decides:

- the smallest shippable slice
- which worker lanes are needed
- what data is allowed
- what external actions are forbidden
- whether a quality eval is needed
- whether an autoreview pass is needed before release
- what proof is required before release

The orchestrator should be willing to say no to impressive-looking work that makes the artifact less useful or less safe.

## Worker Lanes

### Research Worker

Produces the operating brief:

- persona
- manual workflow
- public-safe sample plan
- expected output
- rejection risks

### Builder Worker

Builds the useful core:

- local CLI or tiny app
- deterministic scoring/parsing/transformation
- optional AI judgement layer
- reproducible sample output

### Eval Worker

Tests whether the output is actually better, safer, or more routeable:

- scenario pack
- weighted rubric
- deterministic prechecks
- strategy comparison
- scorecard output
- non-claims for live quality or production routing

### Autoreview Worker

Reviews the integrated artifact against the original brief:

- smallest useful slice
- unnecessary abstractions or dependencies
- broad integrations that should stay out
- AI where deterministic logic would be enough
- proof claims that outrun evidence
- public-safety boundaries

The autoreview worker should be willing to recommend deleting impressive-looking
work if it does not serve the workflow.

### Crabbox Runner

Runs the artifact away from normal workspace assumptions when the proof needs it:

- clean remote execution
- test command output
- browser or desktop evidence when recorded
- screenshots, logs, or test summaries when useful
- cleanup after the run

The public repo names this pattern because Crabbox is public at [crabbox.sh](https://crabbox.sh/), but it does not publish private broker details, provider choices, lease IDs, auth material, project paths, or live evidence.

### QA Worker

Attacks the artifact:

- tests
- eval scorecards
- missing input paths
- bad config
- stale docs
- confusing owner flow
- missing Browser Use or Computer Use tooling for visible proof
- leak-prone files

### Browser E2E Worker

Verifies the user path when browser proof is part of the release:

- page loads
- first-run state is understandable
- form accepts realistic input
- run button executes the same local command path
- output renders clearly
- CSV/download/print flows work

### Computer Use Worker

Verifies visible desktop or OS-level paths when browser control is not enough:

- file pickers
- native dialogs
- generated PDFs or downloads opened visually
- drag/drop paths
- screenshots or artifact notes that are public-safe

Use this only for fake data or approved safe contexts, never private browser
profiles, inboxes, cookies, or real customer systems.

### PR / Ship Worker

Creates the merge-ready shape:

- clean git status
- public safety scan
- generated junk removed
- sample outputs intentional
- no private history

## Why This Matters

Most failed AI prototypes are not model failures. They are operating failures:

- vague brief
- orchestration before the problem is understood
- no deterministic baseline
- no output-quality eval for behavior changes
- no autoreview for scope creep or overengineering
- hidden local state
- no proof chain
- no release hygiene
- UI not actually tested
- accidental secrets or private data

The worker model is designed to make those failures visible before release.
