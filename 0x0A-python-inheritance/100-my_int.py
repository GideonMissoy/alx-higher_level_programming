#!/usr/bin/python3
"""
This module defines a custom integer class `MyInt`.
"""


class MyInt(int):
    """A custom integer class that inverts the `==` and `!=` operators."""
    def __eq__(self, other):
        """Override the default == operator"""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """Override the default != operator"""
        return int.__eq__(self, other)
