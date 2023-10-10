#!/usr/bin/python3
""" Module is_kind_of_class """


def is_kind_of_class(obj, a_class):
    """Function that returns true if an object is
        exactly an instance of a specific class or
        inherited class

        Args:
            obj: represents the object
            a_class: a specific class

        Returns:
            True if is instance of class or false
    """
    return isinstance(obj, a_class)
