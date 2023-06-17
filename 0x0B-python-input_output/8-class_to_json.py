#!/usr/bin/python3
"""
This module contains the function class_to_json
Function returns the dict description eith simple data structure
for JSON serialization of an object
"""

def class_to_json(obj):
    """Returns the dict description with simple data structure."""
    return obj.__dict__
