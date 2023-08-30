#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    number = 0
    density = 0

    i = 0
    while i < len(my_list):
        number += my_list[i][0] * my_list[i][1]
        density += my_list[i][1]
        i += 1

    return (number / density)
