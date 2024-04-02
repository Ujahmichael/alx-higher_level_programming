#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    kase = 0
    for i in range(list_length):
        try:
            kase = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            kase = 0
        except IndexError:
            print("out of range")
            kase = 0
        except ZeroDivisionError:
            print("division by 0")
            kase = 0
        finally:
            result.append(kase)
    return (result)
