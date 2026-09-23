from pathlib import Path

REQUIRED = [
    "src/main.py",
    "src/runtime/executor.py",
    "src/agents/agent_manager.py",
    "src/tools/registry.py",
]

def check_project(root='.'):
    return {p: Path(root, p).exists() for p in REQUIRED}
