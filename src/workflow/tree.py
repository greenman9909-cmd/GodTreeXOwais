class WorkflowNode:
    def __init__(self, name, action=None):
        self.name = name
        self.action = action
        self.children = []

    def add(self, node):
        self.children.append(node)

    def execute(self, context=None):
        result = self.action(context) if self.action else context
        for child in self.children:
            result = child.execute(result)
        return result
