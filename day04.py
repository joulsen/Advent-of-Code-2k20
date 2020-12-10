# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 16:41:32 2020

@author: Andreas J. P.
"""

import re

# Definitions of constants from the exercise
required_field = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

# Loading of file
with open("input/day04.txt") as file:
    # Putting all passports on 1 line
    passports = re.sub(r"(\w)\n(\w)", r"\1 \2", file.read())
    passports = re.sub(r"^\n", "", passports, flags=re.MULTILINE)
    passports = passports.split('\n')


def all_fields_present(passport):
    for field in required_field:
        if field not in passport:
            return False
    return True


def get_field(passport, field):
    result = re.findall(r"{}:([^ ]+)".format(field), passport)[0]
    if field in ["byr", "iyr", "eyr"]:
        return int(result)
    else:
        return result


def hcl_valid(hcl):
    if hcl[0] == "#" and len(hcl) == 7:
        try:
            int(hcl[1:], 16)
            return True
        except ValueError:
            return False
    return False


def hgt_valid(hgt):
    try:
        limits = {"cm": (150, 193), "in": (59, 76)}[hgt[-2:]]
        if (limits[0] <= int(hgt[:-2]) <= limits[1]):
            return True
    except KeyError:
        pass
    return False


def is_valid(passport):
    if not all_fields_present(passport):
        return False
    # BYR, IYR, EYR
    if not (1920 <= get_field(passport, "byr") <= 2002 and
            2010 <= get_field(passport, "iyr") <= 2020 and
            2020 <= get_field(passport, "eyr") <= 2030):
        return False
    # HGT
    if not hgt_valid(get_field(passport, "hgt")):
        return False
    # HCL
    if not hcl_valid(get_field(passport, "hcl")):
        return False
    # ECL
    if not (get_field(passport, "ecl") in ["amb", "blu", "brn",
                                           "gry", "grn", "hzl", "oth"]):
        return False
    if not (get_field(passport, "pid").isnumeric() and
            len(get_field(passport, "pid")) == 9):
        return False
    return True


def part1():
    return sum(all_fields_present(p) for p in passports)


def part2():
    return sum(is_valid(p) for p in passports)


# Printing results
print("Answer to AoC day 4 part 1 is: {}".format(part1()))
print("Answer to AoC day 4 part 2 is: {}".format(part2()))
