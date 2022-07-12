#!/usr/bin/python3
"""Module 7-save_to_json_file.
   Writes an object to a text file,
   Using a JSON representation.
"""


import json


def save_to_json_file(my_obj, filename):
    """Writes the representation of my_obj
    to fiename.

    Args:
        - my_obj: object to write
        - filename: file to write into
    """

    with open(filename, "w+") as f:
        json.dumps(my_obj, f)
