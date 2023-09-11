#!/usr/bin/python3
def multiple_returns(sentence):
    '''
        returns a tuple with the length of a string
        and its first character.
    '''
    len_sentence = len(sentence)
    if not sentence:
        new_tuple = (len_sentence, None)
    else:
        new_tuple = (len_sentence, sentence[0])

    return (new_tuple)

