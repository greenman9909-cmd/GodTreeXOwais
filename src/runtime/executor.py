from dataclasses import dataclass
from typing import Callable, Dict

@dataclass
class Task:
    name: str
    payload: dict

class RuntimeExecutor:
    def __init__(self):
        self.tasks = []
        self.tools: Dict[str, Callable] = {}

    def register_tool(self, name, fn):
        self.tools[name] = fn

    def run(self, task: Task):
        return {"task": task.name, "status": "completed"}
