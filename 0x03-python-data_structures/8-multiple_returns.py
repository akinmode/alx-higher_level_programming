#!/usr/bin/python3
def multiple_returns(sentence):
    """
        Returns a tuple with the length of a string and its first character.
    """
    if sentence is not None and len(sentence) > 0:
        return (len(sentence), sentence[0])
    else:
        return (0, None)
