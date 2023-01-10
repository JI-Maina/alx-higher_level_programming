#!/usr/bin/python3
"""Defines a serialization function."""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string).

    Args:
        my_obj (any): Object to be serialized.
    """
    return json.dumps(my_obj)
