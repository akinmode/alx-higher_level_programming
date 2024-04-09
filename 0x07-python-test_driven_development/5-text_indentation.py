#!/usr/bin/python3
"""Module separates sentences after characters: ., ? and :"""


def text_indentation(text):
    """Separates sentences by characters: ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    end = 0
    textlen = len(text)
    while end < textlen:
        start = end
        while start < textlen and text[start] == ' ':
            start += 1
        end = start
        while (end < textlen and text[end] != '.' and text[end] != ':' and
               text[end] != '?'):
            end += 1
        if end < textlen:
            end += 1
        print(text[start:end], end="")
        end -= 1
        if text[end] == '.' or text[end] == '?' or text[end] == ':':
            print("\n")
        end += 1
