---
name: how-i-engineer-conversation-brief
description: "Use when a user workflow is not yet clear enough to build. Turns the conversation into a tight, worker-ready brief."
---

# Conversation Brief

Use this skill before orchestration or implementation when the ask is still fuzzy.

This is for:

- vague workflow ideas
- early customer/operator conversations
- deciding what not to build
- converting a messy request into a brief another agent can execute

This is not for:

- building code before the workflow is understood
- broad market research
- forcing AI into a workflow that only needs deterministic logic

## Loop

1. Identify the user/persona.
2. Describe the current manual workflow in plain English.
3. Name the repeated pain.
4. Define the input the user already has.
5. Define the output that changes their next action.
6. List forbidden actions and sensitive data boundaries.
7. Decide the smallest useful local version.
8. Define proof: CLI, tests, output inspection, browser, computer, Crabbox, autoreview, or PR/ship safety.
9. Write the brief using `templates/automation-brief.md`.

## Question Discipline

Ask only the smallest number of questions needed to proceed.

Prefer:

- "What input do they already have?"
- "What should they get back?"
- "What should the tool never do automatically?"

Avoid:

- asking for full product strategy
- turning one workflow into a platform
- inventing integrations before the local output is useful

## Output

Return a brief with:

- one-line mission
- user
- current workflow
- input
- output
- deterministic core
- optional AI layer
- safety boundaries
- smoke test
- worker plan
- proof ladder
- limits

If the workflow is still not buildable, say exactly which missing detail blocks it.
