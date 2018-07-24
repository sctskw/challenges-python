#!/usr/bin/python

"""
    ServiceLane Challenge

    https://www.hackerrank.com/challenges/service-lane

"""

import sys

def intify(line):
    """convert line to list of ints"""
    return map(int, line.strip().split(' '))

def run():
    """start tests"""
    lines = sys.stdin.readlines()
    widths = intify(lines[1])

    for test in lines[2:]:
        i, j = intify(test)
        print min(widths[i:j+1])

if __name__ == "__main__":
    run()
