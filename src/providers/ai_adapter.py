class AIProvider:
    def __init__(self, name='local'):
        self.name = name

    def run(self, prompt):
        return {'provider': self.name, 'output': prompt}
