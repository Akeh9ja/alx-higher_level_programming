#!/usr/bin/python3
"""Defines a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to text file using JSON representation"""
    with open(filename, "w") as f:
        json.dumps(my_obj, f)