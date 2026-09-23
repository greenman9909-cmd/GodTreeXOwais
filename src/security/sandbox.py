class Sandbox:
    def __init__(self):
        self.enabled = True

    def validate(self, task):
        return self.enabled and task is not None
