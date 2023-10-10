#!/usr/bin/python3
""" Module inherits_from """


def inherits_from(obj, a_class):
    """Function that returns true if an object is
        an instance of a class that inherits from the
        specified class

        Args:
            obj: represents the object
            a_class: a specific class

        Returns:
            True if is instance of class or false
    """
    if isinstance(obj, a_class):
        return True
    elif (type(obj) == a_class):
        return False
