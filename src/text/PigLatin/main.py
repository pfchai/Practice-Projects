#!/usr/bin/env python
# encoding: utf-8

import string


def create_pig_latin(s):
    vowel = "aeiou"
    addWords = "ay"

    lowStr = s.upper()
    for i, v in enumerate(lowStr):
        if v not in vowel and v in string.ascii_uppercase:
            break
    return s[0:i] + s[i+1:] + "-" + s[i] + addWords


if __name__ == '__main__':
    s = "banana"
    print create_pig_latin(s)
