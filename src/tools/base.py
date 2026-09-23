from abc import ABC, abstractmethod

class Tool(ABC):
    name = "tool"

    @abstractmethod
    def run(self, **kwargs):
        pass

class ToolManager:
    def __init__(self):
        self.tools = {}

    def register(self, tool):
        self.tools[tool.name] = tool

    def execute(self, name, **kwargs):
        return self.tools[name].run(**kwargs)
