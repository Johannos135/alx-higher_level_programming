#!/usr/bin/python3
'''Python module for adding two integers'''
def add_integer(a, b=98):
    '''Takes in a and b and returns the result of a+b

        Args:
            a (int): A number representing the first argument
            b (int): A number representing the second one

        Returns:
            The addition of a and b

        Raises:
            TypeError: if a or b are not integer or float
    '''
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    a = int(a)
    b = int(b)
    return (a + b)
