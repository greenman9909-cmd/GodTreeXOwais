"""Git workspace integration foundation."""

class GitSync:
    def status(self):
        return {"connected": True}

    def prepare_commit(self, message: str):
        return {"message": message}
