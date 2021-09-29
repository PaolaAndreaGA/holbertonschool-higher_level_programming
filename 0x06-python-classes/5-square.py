#!/usr/bin/python3
"""Square class based 4-quare"""


class Square:
    """define Square class"""

    def __init__(self, size=0):
        """initilization Square size"""
        self.__size = size

    @property
    def size(self):
        """to retrieve it"""
        return self.__size

    @size.setter
    def size(self, value):
        """to set it: size must be int, if size is less than 0"""

        if type(value) != int:
            raise TypeError("size must be an integer")

        if value < 0:
                raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
            """calculate the area of a square"""

            return (self.__size * self.__size)

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size > 0:
            for i in range(self.__size):
                    print("#" * self.__size)
            print("")
        if self.__size == 0:
            print("")
