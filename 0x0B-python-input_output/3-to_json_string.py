#!/usr/bin/python3
"""
This module contains the function to_json_string
Function returns the JSON representation of an object.
"""

import json

def to_json_string(my_obj):
    """returns the json representation of an object."""
    return json.dumps(my_obj)
