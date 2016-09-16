#!/usr/bin/env python
# encoding: utf-8

import re

def count_words(s, wordCount={}):
    pa = re.compile(r"\w+")
    for m in pa.finditer(s):
        w = m.group()
        wordCount[w] = wordCount.get(w, 0) + 1
    return wordCount

def count_file_words(fileName):
    wc = {}
    with open(fileName, 'r') as f:
        for line in f.xreadlines():
            wc = count_words(line, wc)
    return wc

if __name__ == '__main__':
    print count_words("hello world hello hi no", {'hello': 1})
    print count_file_words("test.txt")
