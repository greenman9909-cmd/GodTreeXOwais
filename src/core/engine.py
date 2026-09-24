import time


class GodTreeEngine:
    def __init__(self):
        self.agents = []
        self.tools = []
        self.memory = {}
        self.history = []
        self.status = "ready"

    def register_agent(self, agent):
        self.agents.append(agent)

    def register_tool(self, tool):
        self.tools.append(tool)

    def remember(self, key, value):
        self.memory[key] = value

    def execute(self, task):
        self.status = "running"
        started = time.time()

        results = []
        for agent in self.agents:
            try:
                results.append(agent.execute(task))
            except Exception as error:
                results.append({"error": str(error)})

        output = {
            "task": task,
            "results": results,
            "tools_available": len(self.tools),
            "duration": round(time.time() - started, 4),
            "status": "completed"
        }

        self.history.append(output)
        self.status = "ready"
        return output


Engine = GodTreeEngine
