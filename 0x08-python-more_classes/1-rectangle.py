#!/usr/bin/python3
"""Write a class Rectangle that defines a rectangle by: (based on 0-rectangle)"""


class Rectangle:
    """class rectangule 0-rectangle"""
    def __init__(self, width=0, height=0):
        """inicialize method"""
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @height.setter
    def heigth(self, value):
        if type(value) is not int:
            raise TypeError("heigth must be an integer")
        if value < 0:
            raise TypeError("heigth must be >= 0")
        self.__height = value
