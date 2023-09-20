#!/usr/bin/python3
"""Define function"""

def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    text = ""
    with open(filename) as m:
        for dash in m:
            text += dash
            if search_string in dash:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
