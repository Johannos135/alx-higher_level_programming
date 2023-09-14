#!/usr/bin/python3
def uniq_add(my_list=[]):
    som = 0
    for num in set(my_list):
        som += num
    return (som)
