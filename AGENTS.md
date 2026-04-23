# EngineAgent Codex Guide

## Repository Intent

This repository uses a Codex-native multi-agent layer to guide development of a desktop internal-combustion-engine simulation application.

The intended product architecture is:

- A thin desktop GUI that delegates work to application services.
- Reusable core services that run without a GUI.
- Explicit contracts for important inputs, outputs, reports, and artifacts.
- Shared validation and preflight behavior.
- Reproducible simulation, comparison, calibration, and reporting workflows.
- Documentation that stays aligned with implemented behavior.
- Incremental feature evolution without breaking defaults.
- Rigorous physical-model and numerical-method correctness in the simulation core.

The files in `.codex/` define operating guidance for coding agents. They are not product implementation.

## Agent Organization

Agent definitions live in `.codex/agents/`.

- `orchestrator.agent.md` owns routing, delegation order, artifact tracking, process-memory updates, and integration readiness.
- `analysis-spec.agent.md` owns problem framing, requirements, acceptance criteria, and scope.
- `architecture-contracts.agent.md` owns boundaries, service contracts, schemas, artifact shapes, and compatibility decisions.
- `core-solver.agent.md` owns core solver and reusable headless service implementation guidance.
- `physics-numerics-rigor.agent.md` owns physical assumptions, units, invariants, numerical stability, convergence, and scientific acceptance criteria.
- `data-import-benchmark-calibration.agent.md` owns canonical import, benchmark packaging, compare flows, calibration contracts, and report artifacts.
- `desktop-gui.agent.md` owns thin desktop GUI workflows, view behavior, and GUI-facing tests.
- `validation-qa.agent.md` owns preflight, validation strategy, test coverage, artifact checks, and release-quality evidence.
- `reviewer.agent.md` owns independent review for regressions, ownership leakage, architecture drift, and missing evidence.
- `documentation.agent.md` owns user and developer documentation alignment.

Shared instruction files live in `.codex/instructions/`.

Process memory lives in `.process/`.

- `.process/STATUS.md` is the source of truth for current workflow progress.
- `.process/DECISIONS.md` records meaningful architecture and process decisions.
- `.process/NEXT-STEPS.md` records the current execution queue in order.

The `.process/` folder is shared project memory for coding agents. It is not product documentation and should stay concise, operational, and easy to update.

For multi-step work:

- In `new` mode, initialize `.process/STATUS.md` for the incoming workstream before delegation begins.
- In `resume` mode, read `.process/STATUS.md`, `.process/DECISIONS.md`, and `.process/NEXT-STEPS.md` before routing work.
- Keep `.process/*` current as gates close, blockers appear, or scope changes.

## Delegation Order

For feature work, the orchestrator should use this order:

1. Read shared state from `.process/*` and determine whether the task is running in `new` or `resume` mode.
2. `analysis-spec` defines the goal, current behavior, acceptance criteria, and out-of-scope items.
3. Update `.process/STATUS.md` and `.process/NEXT-STEPS.md` when the spec closes or changes the queue.
4. `architecture-contracts` defines service boundaries, contracts, schemas, artifact formats, and compatibility rules.
5. Record meaningful architecture or workflow decisions in `.process/DECISIONS.md`.
6. Involve `physics-numerics-rigor`, `data-import-benchmark-calibration`, and `desktop-gui` only when their ownership is touched.
7. Close the `implementation ready` gate only when the required upstream artifacts are complete and ownership is clear.
8. The implementation owner performs the scoped code change.
9. `validation-qa` verifies preflight, tests, workflows, and artifacts and produces the validation report.
10. `reviewer` performs independent review against contracts, evidence, and ownership rules.
11. `documentation` updates user and developer docs to match the delivered behavior.
12. Refresh `.process/*` whenever a gate closes, a blocker appears, or the workstream is reordered or completed.

The orchestrator may skip agents only when their ownership area is clearly irrelevant and the reason is recorded in the work summary or `.process/STATUS.md`.

## Expected Artifacts

Feature work should produce the smallest useful set of these artifacts:

- Spec note: goal, users, current behavior, acceptance criteria, and out-of-scope items.
- Contract note: service/API boundaries, schemas, artifact formats, defaults, and compatibility notes.
- Rigor checklist: assumptions, units, invariants, expected trends, stability criteria, convergence criteria, and scientific acceptance criteria.
- Data/report spec: import mappings, normalization, benchmark package contents, comparison metrics, calibration flow, and report outputs.
- Validation report: tests run, preflight checks, artifact checks, known gaps, and residual risk.
- Review findings: blocking issues, non-blocking concerns, and approval state.
- Documentation update: user-facing behavior, developer workflow, assumptions, limits, and artifact descriptions.
- Process update: current phase, decisions, next steps, blockers, and validation state in `.process/`.

## Workflow Gates

The orchestrator should use artifact-based gates instead of frontend/backend or other implementation-phase labels.

- `spec ready`: `analysis-spec` has produced an actionable spec note.
- `contracts ready`: `architecture-contracts` has defined the required boundaries, contracts, schemas, defaults, and artifact shapes.
- `rigor checklist ready`: `physics-numerics-rigor` has produced assumptions, units, invariants, expected trends, stability criteria, convergence criteria, and guardrails when solver rigor is touched.
- `data/report contract ready`: `data-import-benchmark-calibration` has defined import, normalization, benchmark, compare, calibration, and report contracts when those workflows are touched.
- `implementation ready`: required upstream artifacts are complete, implementation ownership is clear, and blockers are either resolved or explicitly accepted.
- `validation report ready`: `validation-qa` has produced validation evidence, skipped checks, artifact verification, and residual risk.
- `review clear of blocking findings`: `reviewer` has no unresolved blocking findings.
- `documentation aligned`: `documentation` matches the delivered behavior, contracts, assumptions, limits, and artifact outputs.

## Process Memory Rules

Update `.process/STATUS.md`:

- Before delegation begins for multi-step work.
- After analysis is completed.
- After contracts are defined or changed.
- After a gate closes or reopens.
- After a milestone is implemented.
- After validation or review.
- Whenever blocked or risk state changes.
- Whenever the orchestrator closes, reopens, or reorders a workstream.

Update `.process/DECISIONS.md` when a decision affects architecture, workflow, contracts, ownership, validation strategy, or repository operation. Record date, decision, rationale, and impact.

Update `.process/NEXT-STEPS.md` whenever scope changes, a gate closes, a workstream is reordered, a blocker appears, or immediate follow-ups change. Keep actions concrete, ordered, and assigned to owner agents.

## Done Criteria

Work is done only when:

- Headless execution remains possible for core workflows.
- GUI code remains thin and delegates business logic to services.
- Contracts, schemas, and artifact formats are explicit and updated.
- Validation and preflight behavior covers the changed workflow.
- Physical and numerical acceptance criteria are satisfied for solver changes.
- Import, benchmark, comparison, calibration, and report artifacts are reproducible when touched.
- Documentation matches implemented behavior.
- `.process/STATUS.md`, `.process/DECISIONS.md`, and `.process/NEXT-STEPS.md` are current for multi-step work.
- Review has checked architecture fit, ownership boundaries, tests, artifacts, and docs.
- No stale runtime, model-assignment, or legacy-project assumptions remain in the agent layer.

## Do-Not Rules

- Do not implement product features inside the multi-agent layer.
- Do not add runtime-specific model fields to agent files.
- Do not move business logic into GUI code.
- Do not let contracts, validation, rigor, or report artifacts have hidden ownership.
- Do not use decorative agents without concrete inputs, outputs, boundaries, and done criteria.
- Do not treat physical correctness or numerical stability as generic review concerns; route them through `physics-numerics-rigor`.
- Do not treat data import, benchmarks, comparison, or calibration as solver side work; route them through `data-import-benchmark-calibration`.
- Do not use `.process/` as polished product documentation.
- Do not let `.process/` drift during multi-step work.
- Do not use backend/frontend phase labels as the workflow control mechanism; use artifact gates and evidence instead.
