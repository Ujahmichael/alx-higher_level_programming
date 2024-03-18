#!/usr/bin/python3

import hidden_4
def hidden_42():
    names = dir(hidden_4)
    for name in names:
        if(name[:2] != "__"):
            print(name)

if __name__ == "__main__":
    hidden_42()
