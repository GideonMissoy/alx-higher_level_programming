#!/usr/bin/python3
"""
Contains the class BaseGeometry()
"""


class BaseGeometry:
	"""A class with public attribute area. """

	def area(self):
		"""Raises an exception."""
		raise Exception("area() is not implemented")

	def integer_validator(self, name, value):
		"""
		Validates that a value is an integer greater than 0.
		Raises:
		- TypeError: If the value is not an integer.
		- ValueError: If the value is less than or equal to 0.
		"""

		if type(value) is not int:
			raise TypeError("{:s} must be an integer".format(name))
		if value <= 0:
			raise ValueError("{:s} must be greater than 0".format(name))
