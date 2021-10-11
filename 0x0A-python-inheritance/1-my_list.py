#!/usr/bin/python3
"""class MyList that inherits from list
"""


from typing import List


class MyList(List):
    """class MyList that inherits from list"""


    def print_sorted(self):
        """prints the list, but sorted"""
        print(sorted(self))
