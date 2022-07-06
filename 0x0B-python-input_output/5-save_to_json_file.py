#!/usr/bin/python3
"""Module 5-to_json_string.
Returns the JSON representation of an object.
"""


import json


def save_to_json_file(my_obj, filename):
    """Returns the JSON representation of my_obj.

    Args:
        - my_obj: string to represent

    Returns: JSON representation
    """
    with open(filename, "w") as f:
        json.dumps(my_obj, f)
