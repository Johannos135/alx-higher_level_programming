#!/usr/bin/python3
def no_c(my_string):
    '''removes all characters c and C from a string.'''
    char = my_string[:]
    j = 0
    for i in range(len(my_string)):
        if (my_string[i] == 'c' or my_string[i] == 'C'):
            char = char[:(i - j)] + my_string[(i + 1):]
            j += 1
    return (char)
