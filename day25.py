# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 14:48:54 2022

@author: Andreas J. P.
"""

with open("input/day25.txt") as file:
    pkey_card, pkey_door = map(int, file.read().split('\n')[:-1])

mod = 20201227

def get_loop_size(key):
    for i in range(int(1e8)):
        if pow(7, i, mod) == key:
            return i

part1 = pow(pkey_card, get_loop_size(pkey_door), mod)

# Printing results
print("Answer to AoC day 25 part 1 is: {}".format(part1))