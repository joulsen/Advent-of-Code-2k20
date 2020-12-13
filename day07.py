# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 21:09:33 2020

@author: Andreas J. P.
"""

import re
from functools import lru_cache
from collections import defaultdict

re_bagtype = re.compile(r"^(\w+ \w+)")
re_contains = re.compile(r"(\d)+ (\w+ \w+)")


# Input parsing
with open("input/day07.txt") as file:
    rule_specification = file.readlines()

rules = defaultdict(dict)
for line in rule_specification:
    rule = {}
    for amount, bag in re_contains.findall(line):
        rule[bag] = int(amount)
    rules[re_bagtype.findall(line)[0]] = rule


# Caching for faster results
@lru_cache(maxsize=1024)
def contained_within(bag):
    # This implementation results in a bag containing itself and the end of
    # recursion. This is accounted for in part1() and part2().
    bag_total = set([bag])
    amount_total = 1
    for b, m in rules[bag].items():
        b_r, m_r = contained_within(b)
        # We update bags and amounts from the recursive call.
        bag_total.update(b_r)
        amount_total += m * m_r
    return bag_total, amount_total


def part1():
    return (sum(["shiny gold" in contained_within(b)[0]
                 for b in rules.keys()]) - 1)


def part2():
    return contained_within("shiny gold")[1] - 1


# Printing results
print("Answer to AoC day 7 part 1 is: {}".format(part1()))
print("Answer to AoC day 7 part 2 is: {}".format(part2()))
