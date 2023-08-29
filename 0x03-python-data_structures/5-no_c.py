#!/usr/bin/python3
def no_c(my_string):
    i = 0
    cp = []
    while i < len(my_string):
        if my_string[i] != 'c' and my_string[i] != 'C':
            cp.append(my_string[i])
        i += 1
    return "".join(cp)
