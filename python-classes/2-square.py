#!/usr/bin/python3
"""
Defines a square with size and a method to compute its area.
"""


class Square:
    """Set the area of the square with validation.

            Args:
                value (int): The area value.

            Raises:
                TypeError: If value is not an integer.
                ValueError: If value is less than 0.
            """

    def __init__(self, size=0):
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size * self.__size
