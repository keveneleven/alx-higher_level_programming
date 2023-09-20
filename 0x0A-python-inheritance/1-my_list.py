#!/usr/bin/python3
""" Define an inherited list class MyList class"""

class MyList(list):
    """Sorted printing for the inbuilt list class"""

    def print_sorted(self):
        """Print list in ascending order"""
        print(sorted(self))
