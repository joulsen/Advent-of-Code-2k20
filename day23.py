# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 13:24:54 2022

@author: Andreas J. P.
"""

# Progress bar for convience
from tqdm import tqdm


def play(labels, length, moves):
    M = len(labels)
    cups = {int(n): int(labels[(i + 1) % M]) for i, n in enumerate(labels)}
    if length != len(labels):
        cups[int(labels[-1])] = max(cups) + 1
        for i in range(max(cups) + 1, length + 1):
            cups[i] = i + 1
        cups[length] = 1
    currCup = int(labels[0])
    for i in tqdm(range(moves)):
        p0 = cups[currCup]
        p1 = cups[p0]
        p2 = cups[p1]
        cups[currCup] = cups[p2]
        # We have to minus to and add one for the case dest=1
        dest = ((currCup - 2) % length) + 1
        while dest in [p0, p1, p2]:
            dest = ((dest - 2) % length) + 1
        cups[p2] = cups[dest]
        cups[dest] = p0
        currCup = cups[currCup]
    return cups


labels = "167248359"
game1 = play(labels, len(labels), 100)
game2 = play(labels, int(1e6), int(1e7))

part1 = [game1[1]]
while game1[part1[-1]] != 1:
    part1.append(game1[part1[-1]])
part1 = "".join(map(str, part1))
part2 = game2[1] * game2[game2[1]]

# Printing results
print("Answer to AoC day 23 part 1 is: {}".format(part1))
print("Answer to AoC day 23 part 2 is: {}".format(part2))
