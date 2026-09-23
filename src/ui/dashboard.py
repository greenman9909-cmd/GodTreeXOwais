class Dashboard:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def render(self):
        return {'nodes': self.nodes}
