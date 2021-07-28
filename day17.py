# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 17:38:01 2021

@author: Andreas J. P.
"""

from itertools import product
from collections import defaultdict

grid = defaultdict(bool)

with open("input/day17.txt") as file:
    for y, row in enumerate(file.readlines()):
        for x, state in enumerate(row.strip()):
            grid[(x, y, 0, 0)] = (state == "#")


def get_grid_limits(grid):
    actives = [i for i in grid.items() if i[1]]
    x = [t[0][0] for t in actives]
    y = [t[0][1] for t in actives]
    z = [t[0][2] for t in actives]
    w = [t[0][3] for t in actives]
    return [(min(x)-1, max(x)+2), (min(y)-1, max(y)+2),
            (min(z)-1, max(z)+2), (min(w)-1, max(w)+2)]


def get_active_neighbours(grid, x, y, z, w, hyper=False):
    active = 0
    if hyper:
        dw_range = [-1, 0, 1]
    else:
        dw_range = [0]
    for dw in dw_range:
        for dx, dy, dz in product([-1, 0, 1], repeat=3):
            if not dz == dy == dx == dw == 0:
                active += (grid[x+dx, y+dy, z+dz, w+dw])
    return active


def cycle(grid, hyper=False):
    new_grid = grid.copy()
    grid_limits = get_grid_limits(grid)
    if hyper:
        w_range = grid_limits[3]
    else:
        w_range = (0, 1)
    for w in range(*w_range):
        for z in range(*grid_limits[2]):
            for y in range(*grid_limits[1]):
                for x in range(*grid_limits[0]):
                    neighbors = get_active_neighbours(grid, x, y, z, w, hyper)
                    if grid[(x, y, z, w)] and neighbors not in {2, 3}:
                        new_grid[(x, y, z, w)] = False
                    elif not grid[(x, y, z, w)] and neighbors == 3:
                        new_grid[(x, y, z, w)] = True
    return new_grid


grid_3d = grid.copy()
grid_4d = grid.copy()

for i in range(6):
    grid_3d = cycle(grid_3d)
    grid_4d = cycle(grid_4d, True)

# Printing results
print("Answer to AoC day 17 part 1 is: {}".format(sum(grid_3d.values())))
print("Answer to AoC day 17 part 2 is: {}".format(sum(grid_4d.values())))
