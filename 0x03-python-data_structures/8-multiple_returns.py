#!/usr/bin/python3
def multiple_returns(sentence):
    """
        Returns a tuple with the length of a string and its first character.
    """
    if sentence is not None:
        return (len(sentence), sentence[0])
    else:
        return (0, None)
