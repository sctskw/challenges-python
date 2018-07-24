#!/usr/bin/python
"""
    Gem-Stones Challenge
    https://www.hackerrank.com/challenges/gem-stones

"""

import sys

def clean(value):
    """clean up string value"""
    return value.strip().lower()

def run():
    """initialize challenge"""

    rocks = sys.stdin.readlines()[1:]
    shared = None

    for rock in map(clean, rocks):
        if shared is None:
            #need the first comparison
            shared = set(rock)
        shared = set(shared).intersection(set(rock))

        if len(shared) == 0:
            #no need to check the rest
            break

    print len(list(shared or []))

if __name__ == "__main__":
    run()
