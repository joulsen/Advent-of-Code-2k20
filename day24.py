# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 22:47:05 2022

@author: Andreas J. P.
"""


from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from collections import defaultdict

with open("input/day24.txt") as file:
    instructions = file.read().split('\n')[:-1]

DIR = {"e":  2, "se":  1-1j, "ne":  1+1j,
       "w": -2, "sw": -1-1j, "nw": -1+1j}

def initial_flip(instructions):
    flipped = set()
    for instruction in instructions:
        directions = []
        while instruction:
            if instruction[0] in "ew":
                directions.append(instruction[0])
                instruction = instruction[1:]
            else:
                directions.append(instruction[0:2])
                instruction = instruction[2:]
        
        number = sum([DIR[i] for i in directions])
        if number in flipped:
            flipped.remove(number)
        else:
            flipped.add(number)
    return flipped

tiles = initial_flip(instructions)
part1 = len(tiles)

for i in range(100):
    counter = defaultdict(int)
    for tile in tiles:
        counter[tile] += 0
        for d in DIR.values():
            counter[tile + d] += 1
    for key, value in counter.items():
        if value == 0 or value > 2 and key in tiles:
            tiles.remove(key)
        elif value == 2 and key not in tiles:
            tiles.add(key)

part2 = len(tiles)

# Printing results
print("Answer to AoC day 24 part 1 is: {}".format(part1))
print("Answer to AoC day 24 part 2 is: {}".format(part2))
