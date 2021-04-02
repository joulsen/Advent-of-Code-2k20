# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 12:59:39 2021

@author: super
"""

from collections import defaultdict
from tqdm import tqdm  # For the progress bar

with open("input/day15.txt") as file:
    spoken = list(map(int, file.read().split(',')))
    occurences = defaultdict(list)
    for turn, speak in enumerate(spoken):
        occurences[speak].append(turn)

for i in tqdm(range(30000000)):
    last = spoken[-1]
    if len(occurences[last]) <= 1:
        speak = 0
    else:
        speak = occurences[last][-1] - occurences[last][-2]
    occurences[speak].append(len(spoken))
    spoken.append(speak)

# Printing results
print("\nAnswer to AoC day 15 part 1 is: {}".format(spoken[2020-1]))
print("Answer to AoC day 15 part 2 is: {}".format(spoken[30000000-1]))
