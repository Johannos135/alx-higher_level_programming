#!/usr/bin/python3
""" Module 6-load_from_json_file """
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file

        Args:
            filename: name of the file
    """
    with open(filename, encoding="utf-8") as f:
        json.load(f)
