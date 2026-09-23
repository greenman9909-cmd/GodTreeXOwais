class Agent:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def execute(self, task):
        return {"agent": self.name, "task": task}

class AgentManager:
    def __init__(self):
        self.agents = []

    def register(self, agent):
        self.agents.append(agent)

    def dispatch(self, task):
        return [a.execute(task) for a in self.agents]
