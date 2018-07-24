#!/usr/bin/python
"""
    Chocolate Feast Challenge
    https://www.hackerrank.com/challenges/chocolate-feast

"""

import sys
import math

def clean(value):
    """clean up string value"""
    return value.strip().lower().split(' ')

def do_total(wrappers, rebate, remaining):
    """handle total amount of chocolates"""
    total = 0

    if wrappers > 0:
        total += wrappers
        wrappers += remaining
        total += do_total(wrappers//rebate, rebate, wrappers%rebate)

    return total

def run():
    """initialize challenge"""

    lines = sys.stdin.readlines()[1:]

    for line in map(clean, lines):
        money, cost, wrapper_rebate = line
        print int(do_total(int(money)//int(cost), int(wrapper_rebate), 0))

if __name__ == "__main__":
    run()
