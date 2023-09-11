#!/usr/bin/python3
def multiple_returns(sentence):
    '''
        returns a tuple with the length of a string
        and its first character.
    '''
    first_char = None

    if not sentence:
        first_char = None
    else:
        first_char = sentence[0]

    return (len(sentence), first_char)
