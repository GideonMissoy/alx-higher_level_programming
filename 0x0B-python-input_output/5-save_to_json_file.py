#!/usr/bin/python3
"""
This module contains the function save_to_json_file
Function writes an object to a text file.
"""

import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file."""
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
