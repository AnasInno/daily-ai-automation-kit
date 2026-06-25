# How I Engineer Brief Template

## Problem Conversation

What did the conversation reveal before orchestration?

- who is stuck:
- what they do manually:
- what makes it slow or risky:
- what output changes their next action:
- what the automation must not do:
- what proof would make this trustworthy:

## One-Line Mission

What workflow will this make easier?

## User

Who has the repeated workflow?

## Pain

What manual task are they doing today?

## Current Workflow

What do they open, copy, paste, compare, rewrite, or check?

## Input

What file, text, CSV, PDF, screenshot, or public page does the automation use?

## Output

What should the user get back?

## Deterministic Core

What can work without an API key?

## Optional AI Layer

Where does AI add useful judgement?

## Safety Boundaries

What must the tool never do automatically?

## Smoke Test

What command proves the tool works with sample data?

## Worker Plan

- Conversation summary:
- Orchestrator decision:
- Research worker:
- Builder worker:
- Eval worker, if output quality or routing changed:
- Autoreview worker, before merge candidate:
- QA worker:
- Browser E2E worker, if recorded:
- Computer Use worker, if OS-level proof is required:
- PR/ship worker:

## Proof Ladder

- CLI smoke:
- Unit tests:
- Eval scorecard, if any:
- Sample output:
- Browser proof, if any:
- Computer Use proof, if any:
- Safety scan:

## Limits

What does the tool not handle yet?
