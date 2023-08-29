#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multiple = []
    i = 0
    while i < len(my_list):
        if my_list[i] % 2 == 0:
            multiple.append(True)
        else:
            multiple.append(False)
        i += 1

    return (multiple)
