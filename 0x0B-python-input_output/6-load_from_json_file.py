Your account doesn’t support creating new files within Google Drive. You can still view and edit existing files.Learn more
#!/usr/bin/python3
"""Defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""
    with open(filename) as f:
        return json.load(f)
