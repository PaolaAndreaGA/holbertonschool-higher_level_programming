#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [new if new != search else replace for new in my_list]
