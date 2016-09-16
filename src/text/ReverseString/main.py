#!/usr/bin/env python
# encoding: utf-8


def reverse(string):
    return string[::-1]

if __name__ == '__main__':
    s = raw_input("Input a strings: ")
    print reverse(s)
