# Analysis Spec Instructions

Use these rules when converting a request into an implementable specification.

## Required Practices

- State the goal, user or workflow, current behavior, desired behavior, and acceptance criteria.
- Identify in-scope and out-of-scope work.
- Identify impacted agents and artifacts.
- Separate product intent from implementation design.
- Call out ambiguity only when it cannot be resolved from repository context.
- Tell the orchestrator when analysis is complete so `.process/STATUS.md` and `.process/NEXT-STEPS.md` can be updated.

## Acceptance Checks

- Another coding agent can act on the spec without guessing intent.
- Acceptance criteria are observable and testable.
- Contract, rigor, data workflow, GUI, validation, review, and documentation impacts are identified.
- The `spec ready` gate can be closed with a concrete spec note.
- `.process/STATUS.md` can record the current stage and immediate next owner.

## Do-Not Rules

- Do not redesign architecture in the spec.
- Do not leave acceptance criteria implicit.
- Do not skip out-of-scope notes when the request boundary matters.
