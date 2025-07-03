#!/usr/bin/python3
"""
Defines a square by its size.
"""


class Square:
    """
    Initialize a new Square instance.

            Args:
                size (int): The size of the square (default is 0).

            Raises:
                TypeError: If size is not an integer.
                ValueError: If size is less than 0.
            """

    def __init__(self, size=0):
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
