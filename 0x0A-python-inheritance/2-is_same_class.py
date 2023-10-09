#!/usr/bin/python3
""" Module is_same_class """


def is_same_class(obj, a_class):
    """Function that returns true if an object is
        exactly an instance of a specific class

        Args:
            obj: represents the object
            a_class: a specific class

        Returns:
            True if is instance of class or false
    """
    return (type(obj) == a_class)
