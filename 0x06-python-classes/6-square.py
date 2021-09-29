#!/usr/bin/python3
"""Square class based 5-quare"""


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
        """prints the square"""

        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print("".join([" " for k in range(self.__position[0])]), end="")
            print("".join(["#" for l in range(self.__size)]))

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """setter of __position"""

        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
