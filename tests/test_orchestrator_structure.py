from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_ROOT_FILES = [
    ".gitignore",
    "requirements.txt",
    "requirements-dev.txt",
    "pytest.ini",
    "pyproject.toml",
    "LICENSE",
    "AGENTS.md",
    "README.md",
]

REQUIRED_AGENT_FILES = [
    "orchestrator.agent.md",
    "analysis.agent.md",
    "architect.agent.md",
    "core-solver.agent.md",
    "gui.agent.md",
    "validation.agent.md",
    "reviewer.agent.md",
    "documentation.agent.md",
]


def _frontmatter(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    assert text.startswith("---\n"), f"{path} must start with YAML frontmatter"
    tail = text[4:]
    end = tail.find("\n---\n")
    assert end >= 0, f"{path} must include closing YAML delimiter"
    return tail[:end]


def _get_field(frontmatter: str, field: str) -> str:
    prefix = f"{field}:"
    for line in frontmatter.splitlines():
        if line.startswith(prefix):
            return line.split(":", 1)[1].strip()
    raise AssertionError(f"Missing field '{field}'")


def test_required_root_files_exist():
    for rel in REQUIRED_ROOT_FILES:
        assert (ROOT / rel).is_file(), f"Missing required file: {rel}"


def test_required_instruction_files_exist():
    instruction_files = [
        ".github/copilot-instructions.md",
        ".github/instructions/core-solver.instructions.md",
        ".github/instructions/gui.instructions.md",
        ".github/instructions/qa.instructions.md",
    ]
    for rel in instruction_files:
        assert (ROOT / rel).is_file(), f"Missing required file: {rel}"


def test_agent_files_have_required_frontmatter_fields_and_models():
    expected_models = {
        "orchestrator.agent.md": "claude-sonnet-4.6",
        "analysis.agent.md": "claude-sonnet-4.6",
        "architect.agent.md": "claude-sonnet-4.6",
        "core-solver.agent.md": "claude-sonnet-4.6",
        "validation.agent.md": "claude-sonnet-4.6",
        "reviewer.agent.md": "claude-sonnet-4.6",
        "gui.agent.md": "claude-haiku-4.5",
        "documentation.agent.md": "claude-haiku-4.5",
    }

    for name in REQUIRED_AGENT_FILES:
        path = ROOT / ".github/agents" / name
        assert path.is_file(), f"Missing agent file: {name}"
        frontmatter = _frontmatter(path)
        assert _get_field(frontmatter, "name")
        assert _get_field(frontmatter, "description")
        assert _get_field(frontmatter, "model") == expected_models[name]
        assert "tools:" in frontmatter


def test_orchestrator_references_other_agents():
    orchestrator_path = ROOT / ".github/agents/orchestrator.agent.md"
    frontmatter = _frontmatter(orchestrator_path)

    required_agent_names = [
        "pywavedyn-analysis",
        "pywavedyn-architect",
        "pywavedyn-core-solver",
        "pywavedyn-gui",
        "pywavedyn-validation",
        "pywavedyn-reviewer",
        "pywavedyn-documentation",
    ]

    assert "agents:" in frontmatter
    for agent_name in required_agent_names:
        assert f"- {agent_name}" in frontmatter
