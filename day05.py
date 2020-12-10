# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 21:36:38 2020

@author: Andreas J. P.
"""

import numpy as np

with open("input/day05.txt") as file:
    passes = file.read().split('\n')[:-1]


def split(rows, char):
    splits = np.split(rows, 2)  # Splits into two equal sized arrays
    if char == "F" or char == "L":
        return splits[0]
    else:
        return splits[1]


def get_position(partition):
    rows = np.arange(0, 128)
    columns = np.arange(0, 8)
    for rp in partition[:-3]:
        rows = split(rows, rp)
    for cp in partition[-3:]:
        columns = split(columns, cp)
    return np.array((rows, columns)).T


positions = np.concatenate([get_position(p) for p in passes])
seat_ids = np.sort(np.sum(positions * [8, 1], axis=1))


def part1():
    return np.max(seat_ids)


""" Part 2 works by creating an array with all values from minimum (here: 6)
to maximum (here: 813). By subtracting the seat_ids with this array the new
array 'difference' will be zero until one seat ID is mismatched. From then on
the array will be 1. By taking np.argmin we find the index at where this mis-
match happens and as such find the seat_id + 1. """


def part2():
    difference = seat_ids - np.arange(np.min(seat_ids),
                                      np.max(seat_ids))
    return seat_ids[np.argmax(difference)] - 1


# Printing results
print("Answer to AoC day 5 part 1 is: {}".format(part1()))
print("Answer to AoC day 5 part 2 is: {}".format(part2()))
