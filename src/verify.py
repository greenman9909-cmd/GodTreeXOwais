from pathlib import Path


def verify_project():
    required = [
        'src/main.py',
        'src/core/engine.py',
        'src/runtime/executor.py'
    ]
    return {item: Path(item).exists() for item in required}


if __name__ == '__main__':
    print(verify_project())
