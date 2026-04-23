# Core Solver Instructions

Use these rules when work touches simulation core or reusable application services.

## Required Practices

- Keep solver and service code callable without the desktop GUI.
- Use explicit units and clear names for physical quantities.
- Preserve deterministic execution for tests, reports, and benchmarks.
- Keep numerical methods guarded with tolerances, convergence criteria, and failure behavior from `physics-numerics-rigor`.
- Match contracts from `architecture-contracts`.
- Do not import GUI modules or depend on GUI state.
- Add focused tests for conservation expectations, trend checks, regressions, and service contracts when relevant.

## Acceptance Checks

- Core workflows run headlessly.
- Inputs, outputs, and failures match approved contracts.
- Numerical behavior is deterministic within declared tolerances.
- Physical and numerical acceptance criteria are represented in tests or validation evidence.

## Do-Not Rules

- Do not move business logic into the GUI.
- Do not bypass `physics-numerics-rigor` for solver acceptance.
- Do not treat import, benchmark, compare, or calibration ownership as solver-owned by default.
