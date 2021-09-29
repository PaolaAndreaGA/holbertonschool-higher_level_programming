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

    @property
    def position(self):
        """getter method"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Sets the position value  """

        if (type(value) != tuple or len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(not isinstance(num, int) for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(num < 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
            """calculate the area of a square"""

            return (self.__size * self.__size)

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.size == 0:
            print()
        else:
            a, b = self.position
            for line in range(b):
                print()
            for line in range(self.size):
                print(' ' * a, end='')
                print('#' * self.size)
