# EngineAgent

Multi-agent orchestrator scaffold for **PyWaveDyn** engine simulation development.

## Scope

- 0D thermodynamics modules
- 1D gas dynamics modules
- Coupled 0D/1D workflows
- CLI and GUI integration
- JSON schema contracts
- Pytest-based validation

## Included structure

- Root project configuration (`pyproject.toml`, requirements, pytest, license)
- Copilot repository instructions (`.github/copilot-instructions.md`)
- Domain instructions (`.github/instructions/*.instructions.md`)
- Agent definitions (`.github/agents/*.agent.md`)

## Model assignments

- **Claude Sonnet 4.6**: orchestrator, analysis, architect, core-solver, validation, reviewer
- **Claude Haiku 4.5**: gui, documentation

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
pytest
```
