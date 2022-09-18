#!/usr/bin/python3
def best_score(a_dictionary):

    if a_dictionary:
            return (list(sorted(a_dictionary.keys(), reverse=True))[0])
    else:
        return None
