"""GodTreeXOwais desktop interface layer."""

from datetime import datetime


class GodTreeWindow:
    def __init__(self, engine=None):
        self.title = "GodTreeXOwais"
        self.status = "ready"
        self.engine = engine
        self.logs = []

    def log(self, message):
        entry = f"[{datetime.now().isoformat(timespec='seconds')}] {message}"
        self.logs.append(entry)
        return entry

    def dashboard(self):
        return {
            "app": self.title,
            "status": self.status,
            "agents": len(getattr(self.engine, "agents", [])),
            "tools": len(getattr(self.engine, "tools", [])),
            "logs": len(self.logs),
        }

    def run_task(self, task):
        self.log(f"Task received: {task}")
        if self.engine:
            return self.engine.execute(task)
        return {"task": task, "status": "waiting-for-engine"}

    def run(self):
        self.log("GodTree UI initialized")
        return self.dashboard()


def launch_ui(engine=None):
    return GodTreeWindow(engine).run()


if __name__ == "__main__":
    launch_ui()
