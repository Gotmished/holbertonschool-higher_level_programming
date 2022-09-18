#!/usr/bin/python3
def best_score(a_dictionary):

    if a_dictionary is not None:
        for key in sorted(a_dictionary.keys(), reverse=True):
            return key
    else:
        return None
