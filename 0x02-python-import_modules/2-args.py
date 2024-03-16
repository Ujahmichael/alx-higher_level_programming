#!/usr/bin/python3
import sys
if len(sys.argv) == 1:
    print("0 arguments.")
elif (len(sys.argv)-1) == 1:
    print("{} argument:\n {}: {}".format((len(sys.argv)-1), (len(sys.argv)-1), str(sys.argv)))
else:
    print("{} arguments:\n{}: {}".format((len(sys.argv)-1), (len(sys.argv)-1), str(sys.argv)))
