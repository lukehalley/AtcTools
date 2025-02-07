import json


def loadJson(path: str) -> dict:
    """Load JSON file from the given path."""
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)