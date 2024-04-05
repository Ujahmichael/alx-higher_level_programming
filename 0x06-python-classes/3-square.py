#!/usr/bin/python

"""Define a clase square."""

class Square:

    """initializing the squiare value
        Args:
            size (int): The size of the new square.
        """

    def __init__(self, size=0):
        self.__size = size

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Return area of square"""
        return (self.__size ** 2)
