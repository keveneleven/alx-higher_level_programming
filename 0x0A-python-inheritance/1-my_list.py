#!/usr/bin/python3
"""Define function."""

class MyList(list):

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
