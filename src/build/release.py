"""Release preparation helpers."""

from pathlib import Path


def validate_release(root='.'):
    required = ['src', 'README.md']
    return all(Path(root, item).exists() for item in required)
