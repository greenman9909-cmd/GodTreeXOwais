"""Permission model for GodTreeXOwais tools and agents."""

class PermissionManager:
    def __init__(self):
        self.permissions = {}

    def allow(self, tool, scope="default"):
        self.permissions[tool] = scope

    def can_run(self, tool):
        return tool in self.permissions
