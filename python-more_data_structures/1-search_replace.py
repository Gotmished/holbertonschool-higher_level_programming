#!/usr/bin/python3
def search_replace(my_list, search, replace):

    new_list = []
    for i in range(len(my_list)):
        if my_list[i] == 2:
            new_list.append(89)
        else:
            new_list.append(my_list[i])

    return (new_list)
