"""Coordinates multiple agents inside workflows."""

class Orchestrator:
    def __init__(self, registry=None):
        self.registry = registry or {}

    def register(self, name, agent):
        self.registry[name] = agent

    def execute(self, name, task):
        agent = self.registry[name]
        return agent.run(task)
