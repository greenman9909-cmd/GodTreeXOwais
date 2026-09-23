from dataclasses import dataclass, field
from typing import Any

@dataclass
class Task:
    name: str
    payload: dict[str, Any] = field(default_factory=dict)
    status: str = "pending"

@dataclass
class AgentResult:
    agent: str
    output: Any
    success: bool = True
