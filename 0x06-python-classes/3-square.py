#!/usr/bin/python3
"""Square class based 2-square"""


class Square:
    """define Square class"""

    def __init__(self, size=0):
        """initilization Square size"""

        if type(size) != int:
            raise TypeError("size must be an integer")

        if size < 0:
                raise ValueError("size must be >= 0")

        self.__size = size

        def area(self):
            """calculate the area of a square"""

            return (self.__size * self.__size)
