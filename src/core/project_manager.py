class ProjectManager:
    def __init__(self):
        self.projects = {}

    def register(self, name, path):
        self.projects[name] = path
        return self.projects[name]

    def list_projects(self):
        return self.projects
