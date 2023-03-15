#!/usr/bin/python3

if __name__ == "__main__":

    import sys
    add = 0
    for h in range(len(sys.argv) - 1):
        add += int(sys.argv[h + 1])
    print("{}".format(add))
