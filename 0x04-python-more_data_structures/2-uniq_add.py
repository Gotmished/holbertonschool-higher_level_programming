#!/usr/bin/python3
def uniq_add(my_list=[]):

    listsum = 0
    unique_list = list(set(my_list))
    for i in unique_list:
        listsum = listsum + i
    return (listsum)
