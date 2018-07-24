#!/usr/bin/python
"""
    Utopian Tree Challenge

    https://www.hackerrank.com/challenges/utopian-tree

"""

import sys

DEBUG = False

def debug(value):
    """to stdout if debug is true"""
    if DEBUG:
        print value

def do_height(cycle, height):
    """calculate height in a specific cycle
        - odd cycles double in height
        - even cycles increase by 1
    """
    if not cycle & 1: # -or- cycle % 2 == 0: even number
        debug('Height increased 1 meter')
        return int(height + 1)
    else:
        debug('Height (%s) doubled in size' % height)
        return int(height * 2)

def do_cycles(cycles):
    """loop through cycles to determine the height"""
    height = 1
    if cycles > 0:
        for cycle in xrange(1, cycles+1):
            height = do_height(cycle, int(height))
            debug('Cycle %s: %s' % (cycle, height))

    return height

def run(values):
    """loop through input and initiate cycle calcs for each value"""
    for value in values:
        print do_cycles(int(value.strip()))

if __name__ == "__main__":
    run(sys.stdin.readlines()[1:])
