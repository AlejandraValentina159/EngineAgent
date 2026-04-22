# EngineAgent Roster

This repository defines a multi-agent orchestration layout for PyWaveDyn engine simulation development.

## Agents

- orchestrator.agent.md — Coordinates multi-agent delivery pipeline.
- analysis.agent.md — Converts engine goals into simulation requirements.
- architect.agent.md — Produces architecture, interfaces, and schema plans.
- core-solver.agent.md — Implements 0D thermo + 1D gas-dynamics solver work.
- gui.agent.md — Implements PySide6 GUI workflows.
- validation.agent.md — Executes pytest and validation gates.
- reviewer.agent.md — Performs technical and numerical review.
- documentation.agent.md — Maintains user/developer docs.

## Model policy

- Claude Sonnet 4.6: orchestrator, analysis, architect, core-solver, validation, reviewer
- Claude Haiku 4.5: gui, documentation
