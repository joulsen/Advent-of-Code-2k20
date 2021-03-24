# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 17:55:08 2021

@author: super
"""

with open("input/day11.txt") as file:
    layout = file.read().split('\n')[:-1]


def iteration(layout, infinite_los=False):
    new_layout = []
    for y in range(len(layout)):
        new_row = ""
        for x in range(len(layout[0])):
            # print(layout[y][x])
            if layout[y][x] == ".":
                new_row += "."
            else:
                occupied = 0
                if infinite_los:
                    for ix in [-1, 0, 1]:
                        for iy in [-1, 0, 1]:
                            i = 0
                            while True and not (ix == iy == 0):
                                i += 1
                                if (0 <= x + i*ix < len(layout[0])) and \
                                   (0 <= y + i*iy < len(layout)):
                                    if layout[y+i*iy][x+i*ix] == "#":
                                        occupied += 1
                                        break
                                    elif layout[y+i*iy][x+i*ix] == "L":
                                        break
                                else:
                                    break
                else:
                    for ix in [-1, 0, 1]:
                        for iy in [-1, 0, 1]:
                            if (0 <= x + ix < len(layout[0])) and \
                               (0 <= y + iy < len(layout)) and \
                               not (ix == iy == 0):
                                occupied += (layout[y+iy][x+ix] == "#")
                if layout[y][x] == "L" and occupied == 0:
                    new_row += "#"
                elif layout[y][x] == "#" and occupied >= 4 + int(infinite_los):
                    new_row += "L"
                else:
                    new_row += layout[y][x]
        new_layout.append(new_row)
    return new_layout, layout == new_layout

layout1 = layout.copy()
layout2 = layout.copy()
while True:
    layout1, identical = iteration(layout1, False)
    if identical:
        print(sum([row.count("#") for row in layout1]))
        break
while True:
    layout2, identical = iteration(layout2, True)
    if identical:
        print(sum([row.count("#") for row in layout2]))
        break