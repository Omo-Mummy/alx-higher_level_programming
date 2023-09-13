Your account doesn’t support creating new files within Google Drive. You can still view and edit existing files.Learn more
#!/usr/bin/python3
"""Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """Return the dictionary represntation of a simple data structure."""
    return obj.__dict__
