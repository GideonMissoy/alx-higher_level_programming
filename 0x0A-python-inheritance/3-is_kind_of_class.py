#!/usr/bin/python3
"""
Functions returns True if object is an instance of, or if the object
is an instance of a class that inherited from, the cpecified class:
otherwise False
"""

def is_kind_of_class(obj, a_class):
	"""True if object is an instance of or inherited from a class, else False"""
	return (isinstance(obj, a_class))
