#!/usr/bin/python3
"""
Defines locked class.
"""


class LockedClass:
    """dynammically prevents users from creating new instance attributes."""
    __slot__ = ["first_name"]
