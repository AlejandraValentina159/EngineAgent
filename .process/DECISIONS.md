# Decisions

## 2026-04-23

Decision: Use `.codex/agents/` and `.codex/instructions/` as the active Codex-native multi-agent layer.

Rationale: The repository needs agent guidance that does not imply a legacy runtime-specific setup.

Impact: Legacy agent and instruction files are not part of the active setup.

## 2026-04-23

Decision: Use artifact-based workflow gates instead of backend or frontend phase labels.

Rationale: The current repository needs orchestration rules that fit a desktop simulation application with shared services, explicit contracts, and evidence-driven validation instead of web-app phase language.

Impact: The orchestrator now tracks `spec ready`, `contracts ready`, `rigor checklist ready`, `data/report contract ready` when applicable, `implementation ready`, `validation report ready`, `review clear of blocking findings`, and `documentation aligned`.

## 2026-04-23

Decision: Keep one concrete `physics-numerics-rigor` owner.

Rationale: Physical-model consistency and numerical-method acceptance must be explicit and not diluted into generic QA or review.

Impact: Solver changes require rigor criteria for assumptions, units, invariants, trends, stability, convergence, and guardrails.

## 2026-04-23

Decision: Add `.process/` as shared project memory for multi-step work.

Rationale: Future Codex work needs a concise, repo-local source of truth for phase, decisions, blockers, validation state, and immediate next steps.

Impact: Multi-step work must update `.process/STATUS.md`, `.process/DECISIONS.md`, and `.process/NEXT-STEPS.md` according to `AGENTS.md`.

## 2026-04-23

Decision: Require explicit `new` and `resume` modes for orchestration.

Rationale: Multi-step Codex work needs a simple rule for whether to initialize a fresh workstream or continue from existing repo-local state.

Impact: The orchestrator must initialize `.process/STATUS.md` in `new` mode and must read `.process/*` before delegation in `resume` mode.
