#!/usr/bin/python3
def multiple_returns(sentence):
    len_sentence = len(sentence)
    if not sentence:
        new_tuple = (len_sentence, sentence[0])
    else:
        new_tuple = (len_sentence, None)

    return (new_tuple)
