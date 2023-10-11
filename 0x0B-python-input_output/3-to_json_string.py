#!/usr/bin/python3
""" Module to_json_string.py """
import json


def to_json_string(my_obj):
    """Function that returns a json representation
        of my_obj

        Args:
            my_obj: object

        Returns:
            The json representation of object
    """
    return json.dumps(my_obj)
