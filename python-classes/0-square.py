#!/usr/bin/python3
"""
This is 0-square.py.

This class defines a square's size
"""
class Square:
    """ Defines a square."""

    def __init__(self, size):
        """ Initialize a new square with a given size."""
        self.__size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

               Args:
                   value (int): The size value to set.

               Raises:
                   TypeError: If value is not an integer.
                   ValueError: If value is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

