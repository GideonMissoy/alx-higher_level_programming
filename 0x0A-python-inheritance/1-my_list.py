#!/usr/bin/python3
"""
MyList inherits list
"""


class MyClass(list):
	"""MyClass inherits list."""
	def print_sorted(self):
		"""Prints the list, but sorted in ascending."""
		print(sorted(self))
