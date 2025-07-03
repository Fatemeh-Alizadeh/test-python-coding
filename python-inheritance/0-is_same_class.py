#!/usr/bin/python3
"""
This module check if two objects are exactly the same.
"""

def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is exactly an instance of a_class (not a subclass), False otherwise.
    """
    return type(obj) == a_class
