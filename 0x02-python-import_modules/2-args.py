#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    cmt = (len(sys.argv)-1)
    if cmt == 0:
        nt = "arguments."
        print(f"{cmt} {nt}")
    elif cmt == 1:
        nt = "argument:"
        print(f"{cmt} {nt}\n{cmt}: {str(sys.argv[1:])}")
    else:
        nt = "arguments:"
        for i in cmt:
            print("{cmt} {nt}\n{cmt[i]}: {str(sys.argv[i])}")
