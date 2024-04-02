#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
        print("{}".format(result))
        return (result)
    except ZeroDivisionError:
        result = None
        return (result)
    finally:
        print("Inside result: {}".format(result))
