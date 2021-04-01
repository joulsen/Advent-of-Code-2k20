# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 21:18:33 2021

@author: super
"""

import re
from itertools import product

with open("input/day14.txt") as file:
    program = file.read().split('\n')[:-1]


# See masking 1 and masking 0 below
# https://en.wikipedia.org/wiki/Mask_(computing)
def part1():
    mem = {}
    for line in program:
        if line[5] == "=":
            and_mask = int(line[7:].replace("X", "1"), base=2)
            or_mask = int(line[7:].replace("X", "0"), base=2)
        else:
            adress, value = map(int, re.findall(r"\[(\d+)] = (\d+)", line)[0])
            mem[adress] = (value & and_mask) | or_mask
    return sum(mem.values())


def get_floating_memory(adress, mask):
    masked_adress = ""
    for m, a in zip(mask, "{:0{mw}b}".format(adress, mw=len(mask))):
        translation = {"1": "1", "0": a, "X": "{}"}  # Maybe a bit slow
        masked_adress += translation[m]
    floats = product([0, 1], repeat=masked_adress.count("{}"))
    return [int(masked_adress.format(*f), base=2) for f in floats]


def part2():
    mem = {}
    for line in program:
        if line[5] == "=":
            mask = line[7:]
        else:
            main_adress, value = map(int, re.findall(r"\[(\d+)] = (\d+)", line)[0])
            for adress in get_floating_memory(main_adress, mask):
                mem[adress] = value
    return sum(mem.values())


# Printing results
print("Answer to AoC day 14 part 1 is: {}".format(part1()))
print("Answer to AoC day 14 part 2 is: {}".format(part2()))
