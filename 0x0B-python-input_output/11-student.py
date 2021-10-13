#!/usr/bin/python3
"""class Student"""


class Student:
    """class Student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Public method Retrieves a dictionary
        representation of a Student instance"""
        my_dict = {}
        if attrs is None:
            return self.__dict__
        for attr in attrs:
            if attr in self.__dict__.keys():
                my_dict[attr] = self.__dict__[attr]
        return my_dict

    def reload_from_json(self, json):
        """Public method that replaces all
        attributes of the Student instance"""
        my_old_dict = self.__dict__
        for attr in json.keys():
            for my_old_attr in my_old_dict.keys():
                if attr == my_old_attr:
                    my_old_dict[my_old_attr] = json[attr]
            return my_old_dict
