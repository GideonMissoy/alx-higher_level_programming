#!/usr/bin/python3
"""
This module contains the function from_json_string
Function returns an object rep by a JSON string
"""

import json


def from_json_string(my_str):
    """returns an object represented by a JSON string."""
    return json.load(my_str)
