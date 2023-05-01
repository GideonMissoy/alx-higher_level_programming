#!/usr/bin/python3

"""Defines a locked class."""


class LockedClass:
    """
    Prevents user from dynamically creating new instance attributes,
    except for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
