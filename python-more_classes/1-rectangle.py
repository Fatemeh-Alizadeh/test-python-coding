#!/usr/bin/python3
"""
Defines a class Rectangle.
"""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with optional width and height."""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, width):
        """
        Set the width of the rectangle.

        Args:
            value (int): The width of the rectangle.

        Raises:
             TypeError: If width is not an integer.
             ValueError: If width is less than 0.
        """
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, height):
        """
        Set the height of the rectangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If height is not an integer.
             ValueError: If height is less than 0.
        """
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height

    def area(self):
            """Return the area of the rectangle."""
            return self.__width * self.__height

    def perimeter(self):
            """Return the perimeter of the rectangle."""
            if self.__width == 0 or self.__height == 0:
                return 0
            return 2 * self.__width + 2 * self.__height
