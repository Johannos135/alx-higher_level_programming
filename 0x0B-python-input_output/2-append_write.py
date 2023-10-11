#!/usr/bin/python3
""" Module write_file """


def append_write(filename="", text=""):
    """Function that appends a string to a text file
    and returns the number of characters written

    Args:
        filename: file name of path to the file
        text: text message

    Returns:
        The number of characters
    """
    with open(filename, "a", encoding="utf-8") as my_file:
        return my_file.write(text)
