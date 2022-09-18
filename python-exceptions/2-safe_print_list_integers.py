#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):

    print_count = 0
    try:
        for i in range(0, x):
            print("{:d}".format(my_list[i]), end="")
            print_count = print_count + 1
    except IndexError:
        print()
    except ValueError:
        pass
    except TypeError:
        pass
    print()

    return print_count
