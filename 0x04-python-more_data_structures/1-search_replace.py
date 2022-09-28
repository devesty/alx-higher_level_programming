#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element by another in a new list"""
    if not my_list:
        return my_list

    return [val if val != search else replace for val in my_list]
