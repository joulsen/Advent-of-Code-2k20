# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 13:29:00 2020

@author: Andreas J. P.
"""

with open("input/day1.txt") as file:
    expenses = sorted(list(map(int, file.readlines())))

for e1 in expenses:
    for e2 in expenses:
        if e1 == e2 or e1 + e2 > 2020:
            break
        if e1 + e2 == 2020:
            part1 = e1 * e2
        # Checking if third operand can be found to sum to 2020
        e3 = 2020 - (e1 + e2)
        if e3 in expenses:
            part2 = e1 * e2 * e3

# Printing results
print("Answer to AoC day 1 part 1 is: {}".format(part1))
print("Answer to AoC day 1 part 2 is: {}".format(part2))
