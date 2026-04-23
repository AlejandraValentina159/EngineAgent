# Orchestrator Instructions

Use these rules when coordinating multi-agent work.

## Required Practices

- Start with current repository state, `AGENTS.md`, `.codex/agents/`, `.codex/instructions/`, and `.process/`.
- Determine whether the workstream is in `new` mode or `resume` mode.
- In `new` mode, initialize `.process/STATUS.md` before delegation.
- In `resume` mode, read `.process/STATUS.md`, `.process/DECISIONS.md`, and `.process/NEXT-STEPS.md` before delegation.
- Route work to the smallest set of agents whose ownership is touched.
- Keep delegation order explicit: analysis, contracts, relevant domain owners, implementation owner, validation, review, documentation.
- Use artifact-based gates instead of implementation-phase labels.
- Track these gates explicitly: `spec ready`, `contracts ready`, `rigor checklist ready`, `data/report contract ready` when applicable, `implementation ready`, `validation report ready`, `review clear of blocking findings`, and `documentation aligned`.
- Keep `.process/STATUS.md` current during multi-step work.
- Record meaningful architecture, ownership, validation, or workflow decisions in `.process/DECISIONS.md`.
- Update `.process/NEXT-STEPS.md` when scope, gate state, order, blockers, or milestones change.
- Record skipped agents only when their ownership is clearly irrelevant.
- Close work only after validation, review, documentation, and process-memory state are handled or explicitly marked as not applicable.

## Acceptance Checks

- Every touched responsibility has an owner.
- Required artifacts are named and either produced or marked not applicable.
- Gate status is explicit and evidence-based.
- `.process/` reflects current task, mode, stage, completed artifacts, pending artifacts, blockers, next steps, and validation/review state.
- Final handoff names completed work, checks run, unresolved risk, and remaining queue.

## Do-Not Rules

- Do not delegate by habit; delegate only to owners whose responsibilities are touched.
- Do not use backend/frontend phase names as control flow.
- Do not start implementation while required upstream gates are open.
- Do not leave `.process/*` stale during multi-step work.
