# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 21:15:30 2021

@author: super
"""

import re
from itertools import chain
from collections import defaultdict

with open("input/day16.txt") as file:
    s1, s2, s3 = file.read().split("\n\n")

fields = {}
for line in s1.split('\n'):
    f, x1, x2, x3, x4 = re.findall(r"(\w+ ?\w+): (\d+)-(\d+) or (\d+)-(\d+)",
                                   line)[0]
    fields[f] = set(chain(range(int(x1), int(x2) + 1),
                          range(int(x3), int(x4) + 1)))

all_valids = set(chain(*fields.values()))
owned = list(map(int, s2.split('\n')[1].split(',')))
nearby = list(map(lambda s: list(map(int, s.split(','))),  # A bit weird but ok
                  s3.split('\n')[1:-1]))

del s1, s2, s3, f, x1, x2, x3, x4, file, line  # <3 the variable explorer


def is_valid(ticket, valid_set):
    for value in ticket:
        if value not in valid_set:
            return False, value
    return True, None


def get_valid_tickets(nearby):
    valid_tickets = []
    error_rate = 0
    for ticket in nearby:
        valid, value = is_valid(ticket, all_valids)
        if valid:
            valid_tickets.append(ticket)
        else:
            error_rate += value
    return error_rate, valid_tickets


def get_field_ids(tickets):
    field_ids = defaultdict(set)
    for field, valids in fields.items():
        for i, column in enumerate(zip(*tickets)):
            valid, _ = is_valid(column, valids)
            if valid:
                field_ids[field].update([i])
    return field_ids


def strip_ids(field_ids):
    strip = {}
    while len(field_ids) > 0:
        sfield, scol = min(field_ids.items(), key=lambda t: len(t[1]))
        scol = next(iter(scol))
        strip[sfield] = scol
        field_ids.pop(sfield)
        for possibilities in field_ids.values():
            try:
                possibilities.remove(scol)
            except ValueError:
                pass
    return strip


def part2(strip, owned):
    out = 1
    for col in [x[1] for x in strip.items() if "departure" in x[0]]:
        out *= owned[col]
    return out


error_rate, valid_tickets = get_valid_tickets(nearby)
field_ids = get_field_ids(valid_tickets)
strip = strip_ids(field_ids)

# Printing results
print("\nAnswer to AoC day 16 part 1 is: {}".format(error_rate))
print("Answer to AoC day 16 part 2 is: {}".format(part2(strip, owned)))
