#!/usr/bin/python

"""
  Halloween Party
  https://www.hackerrank.com/challenges/halloween-party
"""

import sys

def do_odd(num):
    """handle odd cuts"""
    return ((num - 1)/2) * ((num + 1)/2)

def do_even(num):
    """handle even cuts"""
    return (num/2) * (num/2)

def do_cuts(cuts):
    """handle number of cuts"""
    if cuts % 2 == 0:
        return do_even(cuts)
    return do_odd(cuts)

def clean(val):
    """convert string to int removing whitespace"""
    return int(val.strip())

def run():
    """initialize challenge"""
    cuts = map(clean, sys.stdin.readlines()[1:])

    for cut in cuts:
        print do_cuts(cut)

if __name__ == "__main__":
    run()
