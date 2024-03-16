#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    add_ = 0
    ct = len(sys.argv)
    for i in range(1, ct):
        add_ += int(sys.argv[i])
    print(f"{add_}")
