# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 15:58:40 2020

@author: Andreas J. P.
"""

import numpy as np

with open("input/day3.txt") as file:
    terrain = np.array((list(map(list, file.readlines()))))


def ride(delta_x, delta_y):
    x = y = 0
    encounters = 0
    while y < terrain.shape[0] - 1:
        # Remark here: -1 because of parsing error
        # Also, % (MODULO) to wrap around horizontally
        x = (x + delta_x) % (terrain.shape[1] - 1)
        y += delta_y
        if terrain[y, x] == '#':
            encounters += 1
    return encounters


def part1():
    return ride(3, 1)


def part2():
    result = 1
    for dx, dy in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        result *= ride(dx, dy)
    return result


# Printing results
print("Answer to AoC day 3 part 1 is: {}".format(part1()))
print("Answer to AoC day 3 part 2 is: {}".format(part2()))
