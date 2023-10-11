#!/usr/bin/python3
""" Module 4-from_json_string """
import json


def from_json_string(my_str):
    """Function that returns an object representation

        Args:
            my_str: json string

        Returns:
            Object represention by a json string
    """
    return json.loads(my_str)
