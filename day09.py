# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 19:20:18 2020

@author: Andreas J. P.
"""

import numpy as np
preamble_length = 25
with open("input/day09.txt") as file:
    # Have to do dtype=float here as numpy doesn't allow for so large integers
    # to be read as C longs.
    transmission = np.array(file.read().split('\n')[:-1], dtype=np.int64)


def get_sums(numbers, repeats=False):
    """
    Produces the vector of all possible sums made from any two numbers found
    in the input. For an explanation of how it works see the file 'day09.md'
    """
    sums = np.add(*np.meshgrid(numbers, numbers))
    sums = np.triu(sums)
    np.fill_diagonal(sums, 0)
    sums = sums.flatten()
    mask = sums != 0
    return sums[mask]


def get_invalid(parsed, unparsed):
    for number in unparsed:
        sums = get_sums(parsed)
        if number not in sums:
            return int(number)
        parsed = np.delete(parsed, 0)
        parsed = np.append(parsed, number)


def part1():
    # Splitting the transmission into an parsed and unparsed at preamble
    # length.
    return get_invalid(*np.split(transmission, [preamble_length]))


def get_continous_sum_to(target):
    possible = transmission[transmission <= target]
    for i in range(len(possible)):
        j = i + 1
        while True:
            cont = possible[i:j]
            contsum = np.sum(cont)
            if contsum < target:
                j += 1
            elif contsum == target:
                return cont
            else:
                break


def part2():
    cont = get_continous_sum_to(part1())
    return np.min(cont) + np.max(cont)


# Printing results
print("Answer to AoC day 2 part 1 is: {}".format(part1()))
print("Answer to AoC day 2 part 2 is: {}".format(part2()))
