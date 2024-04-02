#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
        print("{}".format(result))
        return (a / b)
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
