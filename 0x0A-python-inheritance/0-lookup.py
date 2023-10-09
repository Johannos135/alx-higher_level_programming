#!/usr/bin/python3
"""Module lookup"""


def lookup(obj):
    """Function that returns a list of available
        attributes and methods of obj

        Args:
            obj: instance of the object

        Returns:
            List of attributes and methods
    """
    return dir(obj)
