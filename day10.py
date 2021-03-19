# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 22:12:44 2021

@author: super
"""

from collections import defaultdict

with open("input/day10.txt") as file:
    adapters = list(map(int, file.readlines()))

adapters = [0] + sorted(adapters) + [max(adapters) + 3]


def part1(adapters):
    diffs = []
    while True:
        prev = adapters.pop(0)
        diffs.append(adapters[0] - prev)
        if len(adapters) == 1:
            break
    return diffs.count(1) * diffs.count(3)


def part2(adapters):
    plugins = defaultdict(int)
    plugins[0] = 1
    for x in adapters:
        plugins[x + 1] += plugins[x]
        plugins[x + 2] += plugins[x]
        plugins[x + 3] += plugins[x]
    return plugins[max(adapters)]


# Printing results
print("Answer to AoC day 10 part 1 is: {}".format(part1(adapters.copy())))
print("Answer to AoC day 10 part 2 is: {}".format(part2(adapters.copy())))
