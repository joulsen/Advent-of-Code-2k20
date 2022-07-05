# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 21:18:46 2022

@author: Andreas J. P.
"""

import re

with open("input/day19.txt") as file:
    rules_data, messages = file.read().split("\n\n")
    messages = messages.split('\n')[:-1]
    rules = {}
    for line in rules_data.split('\n'):
        k, v = line.strip().split(':')
        v = v.replace('"', '')
        if '|' in v:
            v = "(?: {} )".format(v)
        rules[k] = v.split()


# While digits in the rule, replace the first occuring digit with the
# corresponding rule. Finally prepend and append ^, $ to only match lines
# of correct length.
def get_re(rules):
    base = rules['0'].copy()
    # While digits in the rule
    while any(x.isdigit() for x in base):
        for i, part in enumerate(base):
            if part.isdigit():
                base[i:i+1] = rules[part].copy()
    return re.compile("^{}$".format(''.join(base)))


rules1 = rules.copy()
part1 = sum(bool(get_re(rules1).match(m)) for m in messages)


rules2 = rules.copy()
# Rule 8: (42 | 42 8) is simply 42 repeating.
rules2['8'] = ["(?:", "42", ")+"]
# Rule 11: (42 31 | 42 11 31) is the following sequence:
# 42 31 OR 42 42 31 31 OR 42 42 42 31 31 31 ... etc. repeating forever
# I generate 100 of these hoping for the best since re library does not support
# recursive regex.
rules2["11"] = ["(?:"]
for i in range(1, 10):
    count = "{{{}}}".format(i)
    s = ["(?:", "(?:", "42", ')', count, "(?:", "31", ')', count, ')', '|']
    rules2["11"] += s
rules2["11"].pop()  # removing last '|'
rules2["11"] += ')'


rules_re_2 = get_re(rules2)
part2 = sum(bool(rules_re_2.match(m)) for m in messages)

# Printing results
print("Answer to AoC day 19 part 1 is: {}".format(part1))
print("Answer to AoC day 19 part 2 is: {}".format(part2))
