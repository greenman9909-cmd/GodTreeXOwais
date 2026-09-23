from pathlib import Path

REQUIRED = [
    'src',
    'desktop',
    'tests'
]


def verify_structure(root='.'):
    base = Path(root)
    return {item: (base / item).exists() for item in REQUIRED}
