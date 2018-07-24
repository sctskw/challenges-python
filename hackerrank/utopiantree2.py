#!/usr/bin/python

for line in range(input()):
    cycles = input()
    height = 1

    for cycle in xrange(1, cycles+1):
        if cycle & 1:
            height*=2
        else:
            height+=1
    print height
