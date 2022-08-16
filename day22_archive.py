# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 10:47:12 2022

@author: Andreas J. P.
"""

from collections import deque

labels = "389125467"
# labels = "167248359"
M = len(labels)
cups = {int(n):int(labels[(i + 1) % M]) for i, n in enumerate(labels)}

currCup = 3

def print_cups(cups, startCup):
    print(startCup, end = " ")
    cup = startCup
    while True:
        cup = cups[cup]
        if cup == startCup:
            break
        print(cup, end=" ")
        
# currCup = 3
# for i in range(100):
#     print("\n{:2}: ".format(i + 2), end="")
#     p0 = cups[currCup]
#     p1 = cups[p0]
#     p2 = cups[p1]
#     destCup = currCup - 1
#     while destCup in (p0, p1, p2) or destCup <= 0:
#         destCup -= 1
#         if destCup < 1: destCup = M
#     cups[currCup] = cups[p2]
#     currCup = cups[p2]
#     cups[p2] = cups[destCup]
#     cups[destCup] = p0
#     print_cups(cups, currCup)

# order = [1]
# for i in range(M - 1):
#     order.append(cups[order[-1]])
# part1 = "".join(map(str, order[1:]))