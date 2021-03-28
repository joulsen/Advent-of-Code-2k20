# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 17:31:08 2021

@author: super
"""

import numpy as np

with open("input/day13.txt") as file:
    depature, lines, _ = file.read().split('\n')
    depature = int(depature)
    lines = np.array(lines.split(','))
    ins = np.array([int(b) for b in lines if b != "x"])


def part1(dep, ins):
    deps_near = np.floor_divide(dep, ins) * ins + ins
    dep_near = np.min(deps_near)
    return ins[np.argmin(deps_near)] * (dep_near - dep)


# Read day13.md for an explanation
def part2(ins):
    offsets = np.argwhere(lines != "x")
    interval = np.int64(1)
    t = np.int64(0)
    for offset, bus in zip(offsets, ins):
        while True:
            if (t + offset) % bus == 0:
                interval *= bus
                break
            t += interval
    return t


# Printing results
print("Answer to AoC day 12 part 1 is: {}".format(part1(depature, ins)))
print("Answer to AoC day 12 part 2 is: {}".format(part2(ins)))
