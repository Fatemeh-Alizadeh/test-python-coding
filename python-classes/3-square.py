#!/usr/bin/python3
"""
Defines a square with size and a method to compute its area.
"""


class Square:

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """
        Get the current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        Set the size of the square with proper validation.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Return the current square area.
        """
        return self.__size * self.__size
