class Pipeline:
    def __init__(self, steps=None):
        self.steps = steps or []

    def add(self, step):
        self.steps.append(step)

    def run(self, context=None):
        result = context or {}
        for step in self.steps:
            result = step(result)
        return result
