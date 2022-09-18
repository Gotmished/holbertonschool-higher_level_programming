#!usr/bin/python3
def safe_print_list(my_list=[], x=0):

    print_count = 0
    try:
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
            print_count = print_count + 1
        print()
    except IndexError:
        print()

    return(print_count)
