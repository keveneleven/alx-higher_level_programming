#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


def print_stats(size, status_codes):
    """Print accumulated metrics.

    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for dash in sys.stdin:
            if num == 10:
                print_stats(size, status_codes)
                num = 1
            else:
                num += 1

            dash = dash.split()

            try:
                size += int(dash[-1])
            except (IndexError, ValueError):
                pass

            try:
                if dash[-2] in valid_codes:
                    if status_codes.get(dash[-2], -1) == -1:
                        status_codes[dash[-2]] = 1
                    else:
                        status_codes[dash[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
