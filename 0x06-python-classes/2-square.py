#!/usr/bin/python3

"""Define a class Square."""

class Square:

    """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """

    def __init__(self, size=0):

        self.__size = size

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
