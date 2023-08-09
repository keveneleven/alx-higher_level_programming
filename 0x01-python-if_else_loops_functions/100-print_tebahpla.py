#!/usr/bin/python3
i = 0
c = ord('z')

while c >= ord('a'):
    print(chr(c - (32 if (c - ord('a')) % 2 == 0 else 0)), end="")
    c -= 1
