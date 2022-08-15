# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 14:39:07 2022

@author: Andreas J. P.
"""

import re
MATCH = re.compile(r"((?:\w+ ?)+) \(contains ((?:\w+,? ?)+)")

with open("input/day21.txt") as file:
    data = file.read()
    foods = data.split('\n')[:-1]

index = {}
words = []
for food in foods:
    food, allergens = food.split(" (contains ")
    words += food.split(' ')
    food = set(food.split(' '))
    allergens = allergens[:-1].split(', ')
    for allergen in allergens:
        if allergen in index:
            index[allergen] = index[allergen] & food
        else:
            index[allergen] = food

index = index.items()
while True:
    for allergen, foods in index:
        if len(foods) == 1:
            for a, f in index:
                if len(f) > 1 and list(foods)[0] in f:
                    f.remove(list(foods)[0])
    if all([len(i[1]) == 1 for i in index]):
        break

index = {a:list(f)[0] for a, f in index}

part1 = len([w for w in words if w not in index.values()])
part2 = ",".join([i[1] for i in sorted(index.items())])

# Printing results
print("Answer to AoC day 21 part 1 is: {}".format(part1))
print("Answer to AoC day 21 part 2 is: {}".format(part2))
