"""Policy engine for controlling agent execution permissions."""

class PolicyEngine:
    def __init__(self):
        self.rules = {}

    def allow(self, action: str):
        self.rules[action] = True

    def can_execute(self, action: str) -> bool:
        return self.rules.get(action, False)
