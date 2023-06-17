#!/usr/bin/python3
"""
This module contains the function load_from_json_file
Function creates an object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """creates an obj from a json file"""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
