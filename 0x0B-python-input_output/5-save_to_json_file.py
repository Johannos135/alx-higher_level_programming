#!/usr/bin/python3
""" Module 5-save_to_json_file """
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using
        a JSON representation

        Args:
            my_obj: object
            filename: name of the file
    """
    with open(filename, "w", encoding="utf-8") as my_file:
        json.dump(my_obj, my_file)
