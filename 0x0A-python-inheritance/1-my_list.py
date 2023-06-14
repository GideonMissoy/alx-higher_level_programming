#!/usr/bin/python3
"""
MyList inherits list
"""


class MyClass(list):
	"""Subclass of list initializer."""

	def __init__(self):
		"""Initializes the object we have."""

		super().__init__()
	
	def print_sorted(self):
		"""Prints the list, but sorted in ascending."""
		print(sorted(self))

