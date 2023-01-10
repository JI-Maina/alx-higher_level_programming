#!/usr/bin/python3
"""Defines a deserialization module."""
import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file.

    Args:
        filename : json file.
    """
    with open(filename) as f:
        return json.load(f)
