#!/usr/bin/python3
""" Module read_line to read text file """


def read_file(filename=""):
    """Function that reads a text file(UTF8) and
        prints it to stdout.

        Args:
            filename: name of the file

        Returns:
            Prints each line
    """
    with open(filename, encoding="utf-8") as my_file:
        for f in my_file:
            print(f.read())
