#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)
    i = 0
    while i < len(names):
        name = names[i]
        if name[:2] != "__":
            print(name)
        i += 1
