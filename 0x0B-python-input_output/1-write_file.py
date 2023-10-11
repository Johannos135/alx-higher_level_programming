#!/usr/bin/python3
""" Module write_file """


def write_file(filename="", text=""):
    """Function that writes a string to a text file
    and returns the number of characters written

    Args:
        filename: file name of path to the file
        text: text message

    Returns:
        The number of characters
    """
    counter = 1 
    count = 0

    with open(filename, "w", encoding="utf-8") as my_file:
        my_file.write(text)

    with open(filename, encoding="utf-8") as my_file:
        while True:
            line = my_file.read()

            if not line:
                break

            for word in line:
                for char in word:
                    count += 1
            counter += 1
    return count
