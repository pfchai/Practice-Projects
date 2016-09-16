#!/usr/bin/env python
# encoding: utf-8

import math

def check_palindrome(s):
    n = int(math.floor(len(s) / 2.0))
    for i in range(n):
        if not s[i] == s[-i-1]:
            return False
    return True


if __name__ == '__main__':
    print check_palindrome("hello")
    print check_palindrome("ollo")
    print check_palindrome("olxlo")

