#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    biggest = my_list[0]
    i = 0
    while i < len(my_list):
        if my_list[i] > biggest:
            biggest = my_list[i]
        i += 1

    return (biggest)
