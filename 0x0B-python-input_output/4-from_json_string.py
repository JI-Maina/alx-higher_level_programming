#!/usr/bin/python3
"""Defines a deserialization function."""
import json


def from_json_string(my_str):
    """Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str (json str): json str to be decoded.
    """
    return json.loads(my_str)
