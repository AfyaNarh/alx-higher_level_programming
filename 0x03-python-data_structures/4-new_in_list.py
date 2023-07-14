#!/usr/bin/python3

def new_in_list(my_list, idx, el):
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = el
    return my_list
