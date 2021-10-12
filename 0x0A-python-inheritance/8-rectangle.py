#!/usr/bin/python3
"""Write an class
"""


class BaseGeometry:
    """Class that defines a shape
    """

    pass

    def area(self):
        """Calculates Area
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function valide type object
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """class Rectangle
    """
    def __init__(self, width, height):
        """Initializes the subclass
        """
        self.integer_validator("width",width)
        self.__width = width

        self.integer_validator("heigth",height)
        self.__heigth = height
