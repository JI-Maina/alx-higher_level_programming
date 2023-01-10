#!/usr/bin/python3
"""Defines a serialization module."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation.

    Args:
        my_obj (any): python obj to be serialized.
        filename (json): file to write Json data.
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
