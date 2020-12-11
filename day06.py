# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 23:10:25 2020

@author: Andreas J. P.
"""

with open("input/day06.txt") as file:
    forms = file.read().split("\n\n")


def part1():
    return sum([len(set(f.replace("\n", ""))) for f in forms])


def part2():
    total = 0
    for form in forms:
        intersections = set.intersection(*map(set, form.split()))
        total += len(intersections)
    return total


# Printing results
print("Answer to AoC day 5 part 1 is: {}".format(part1()))
print("Answer to AoC day 5 part 2 is: {}".format(part2()))
