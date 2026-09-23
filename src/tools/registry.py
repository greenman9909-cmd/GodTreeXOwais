class ToolRegistry:
    def __init__(self):
        self.tools = {}

    def register(self, name, handler):
        self.tools[name] = handler

    def execute(self, name, *args, **kwargs):
        if name not in self.tools:
            raise ValueError(f"Unknown tool: {name}")
        return self.tools[name](*args, **kwargs)
