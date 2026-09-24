"""GodTree agent management layer."""

from datetime import datetime


class Agent:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.active = True
        self.history = []

    def execute(self, task):
        result = {
            "agent": self.name,
            "role": self.role,
            "task": task,
            "status": "completed",
            "time": datetime.now().isoformat(timespec="seconds"),
        }
        self.history.append(result)
        return result


class AgentManager:
    def __init__(self):
        self.agents = []

    def register(self, agent):
        self.agents.append(agent)

    def dispatch(self, task):
        return [agent.execute(task) for agent in self.agents if agent.active]

    def status(self):
        return {
            "agents": len(self.agents),
            "active": len([a for a in self.agents if a.active]),
        }
