Your account doesn’t support creating new files within Google Drive. You can still view and edit existing files.Learn more
#!/usr/bin/python3
"""Defines a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of a string object."""
    return json.dumps(my_obj)
