#!/usr/bin/python

"""THIS PYTHON CODE IS WRITTEN BY UJAH MICHAEL(MAJESTI)"""

"""Define a clase square."""

class Square:
    """initializing the squiare value
        Args:
            size (int): The size of the new square.
        """
    def __init__(self, size=0):
        self.size = size
    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        """Return area of square"""
        return (self.__size ** 2)
