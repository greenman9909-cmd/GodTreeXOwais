import subprocess

class GitManager:
    def status(self):
        return subprocess.getoutput('git status')

    def commit_message(self, message):
        return message
