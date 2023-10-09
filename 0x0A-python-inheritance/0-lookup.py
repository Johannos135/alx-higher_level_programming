#!/usr/bin/python3
def lookup(obj):
    """Function that returns a list of available attributes
        and methods of obj

        Args:
            obj: instance of the object

        Returns:
            List of available attributes and methods
    """
    return (dir(obj))
