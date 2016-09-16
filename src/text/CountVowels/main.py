#!/usr/bin/env python
# encoding: utf-8

def count_vowels(s):
    vowels = "AEIOU"
    upperStr = s.upper()

    return len(filter(lambda w: w in vowels, upperStr))


def count_vowels_more(s):
    vowels = "AEIOU"
    upperStr = s.upper()
    vowelsCount = {}
    for v in vowels:
        vowelsCount[v] = upperStr.count(v)

    return vowelsCount


if __name__ == '__main__':
    print count_vowels("hello")
    for k, v in count_vowels_more("hello").iteritems():
        print k + ": " + str(v)
