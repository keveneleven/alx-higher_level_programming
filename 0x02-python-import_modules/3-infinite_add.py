#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    tot = 0
    i = 0
    cnt = len(sys.argv) - 1
    while i < cnt:
        tot += int(sys.argv[i + 1])
        i += 1
        print("{}".format(tot))
