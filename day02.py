# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 15:37:53 2020

@author: Andreas J. P.
"""

import re
parser = re.compile(r"(\d+)-(\d+) (\w): (\w+)")

with open("input/day02.txt") as file:
    database = parser.findall(file.read())


def part1():
    return sum([1 for lower, upper, char, pw in database
                if int(lower) <= pw.count(char) <= int(upper)])


def part2():
    return sum([1 for first, second, char, pw in database
                if (pw[int(first) - 1] == char) ^  # XOR
                (pw[int(second) - 1] == char)])


# Printing results
print("Answer to AoC day 2 part 1 is: {}".format(part1()))
print("Answer to AoC day 2 part 2 is: {}".format(part2()))
