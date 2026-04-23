# Physics Numerics Rigor Instructions

Use these rules when work changes or evaluates solver physics, numerical methods, or scientific acceptance.

## Required Practices

- State physical-model assumptions and limits.
- State units, dimensions, invariants, and conservation expectations.
- Define expected physical trends for changed behavior.
- Define numerical stability and convergence criteria.
- Define tolerances and guardrails for invalid or non-physical states.
- Define sanity checks that validation can run.
- Reject solver changes that lack scientific acceptance criteria.

## Acceptance Checks

- Assumptions and limits are visible to developers and documenters.
- Units and invariants are testable.
- Convergence and stability criteria are explicit.
- Failure behavior for non-physical or unstable states is defined.
- Solver approval is tied to evidence, not intuition.
- The `rigor checklist ready` gate can be closed with explicit scientific acceptance criteria.

## Do-Not Rules

- Do not act as generic QA.
- Do not approve solver changes based only on software tests.
- Do not leave units, invariants, stability criteria, or convergence criteria implicit.
