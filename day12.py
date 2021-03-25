# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 08:14:05 2021

@author: super
"""

import numpy as np

with open("input/day12.txt") as file:
    actions = list(map(lambda s: (s[0], s[1:]), file.read()[:-1].split('\n')))

position = np.array([0, 0])
waypoint = np.array([10, 1])
direction = 90


def part1(actions, position, direction):
    for action, value in actions:
        value = int(value)
        if action == "F":
            direction = direction % 360
            action = {0: "N", 90: "E", 180: "S", 270: "W"}[direction]
        elif action == "L":
            direction -= value
        elif action == "R":
            direction += value
        if action in "NESW":
            position += value * np.array({"N": [0, 1], "E": [1, 0],
                                          "S": [0, -1], "W": [-1, 0]}[action])
    return np.sum(np.abs(position))


def part2(actions, position, waypoint):
    for action, value in actions:
        value = int(value)
        if action == "F":
            position += value * waypoint
        elif action == "R":
            for i in range(value // 90):
                waypoint = np.array([waypoint[1], -waypoint[0]])
        elif action == "L":
            for i in range(value // 90):
                waypoint = np.array([-waypoint[1], waypoint[0]])
        elif action in "NESW":
            waypoint += value * np.array({"N": [0, 1], "E": [1, 0],
                                          "S": [0, -1], "W": [-1, 0]}[action])
    return np.sum(np.abs(position))


answer1 = part1(actions, np.array([0, 0]), 90)
answer2 = part2(actions, np.array([0, 0]), np.array([10, 1]))

# Printing results
print("Answer to AoC day 12 part 1 is: {}".format(answer1))
print("Answer to AoC day 12 part 2 is: {}".format(answer2))
