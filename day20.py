# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 15:02:21 2022

@author: Andreas J. P.
"""

from collections import defaultdict
from math import sqrt, prod
from PIL import Image, ImageDraw
import sys

DEBUG = True
sys.stdout = open("day20log.txt", "w")

def flip(tile):
    return "\n".join(map(lambda s: s[::-1], tile.split('\n')))

def rotate(tile):
    lines = []
    for i in range(M):
        lines.append("".join([tile[i+(M+1)*j] for j in range(M)])[::-1])
    return "\n".join(lines)

def get_side(tile, side):
    M = len(t.splitlines()[1])
    if side == "up":
        return tile[:M]
    elif side == "down":
        return tile[M*M-1:]
    elif side == "right":
        return "".join([tile[M-1+(M+1)*j] for j in range(M)])
    elif side == "left":
        return "".join([tile[0+(M+1)*j] for j in range(M)])

def get_sides(tile):
    sides = [get_side(tile, d) for d in ["up", "down", "right", "left"]]
    # sides += 
    return sides + [s[::-1] for s in sides]

def is_aligned(t1, t2, direction):
    if direction == "north":
        s1 = get_side(t1, "up")
        s2 = get_side(t2, "down")
    elif direction == "east":
        s1 = get_side(t1, "right")
        s2 = get_side(t2, "left")
    elif direction == "south":
        return is_aligned(t2, t1, "north")
    elif direction == "west":
        return is_aligned(t2, t1, "east")
    return s1 == s2

def get_iterations(tile):
    iterations = [tile]
    for i in range(8):
        iterations.append(rotate(iterations[-1]))
        if i == 4:
            iterations[-1] = flip(iterations[-1])
    return iterations

def align(t1, t2, direction):
    if len(t1) != len(t2):
        return False
    for t2 in get_iterations(t2):
        if is_aligned(t1, t2, direction):
            return t2
    return False

def align_grid(tile, c):
    x, y = c
    if c == (0, 0):
        return True
    if c[1] == 0:
        return align(grid[x-1, y], tile, "east")
    if c[0] == 0:
        return align(grid[x, y-1], tile, "south")
    else:
        up = align(grid[x, y-1], tile, "south")
        left = align(grid[x-1, y], tile, "east")
        if up and left:
            return left


def console_log(string, end="\n"):
    if DEBUG:
        print(string, end=end)
        
def get_next_coord(c):
    x, y = c
    if x == T-1:
        return (0, y+1)
    else:
        return (x+1, y)

def get_corners():
    neighbors = defaultdict(int)
    for ID1, t1 in tiles.items():
        for ID2, t2 in tiles.items():
            neighbors[ID1] += any([s in sides[ID2] for s in sides[ID1]])
        neighbors[ID1] -= 1
    return [ID for ID, n in neighbors.items() if n == 2]

def solve(c):
    if c not in IDs.values():
        # If ANY ID is currently in the grid (i.e. grid is nonempty)
        if any(IDs.values()):
            for ID, tile in tiles.items():
                if ID in IDs.values():
                    pass
                else:
                    # Returns false if the tile cannot be aligned in the grid
                    tile = align_grid(tile, c)
                    if tile:
                        console_log("{} | Tile #{} ".format(c, ID), end="")
                        console_log("[Alignable]")
                        IDs[c] = ID
                        grid[c] = tile
                        console_log("")
                        solve(get_next_coord(c))
                        if all(IDs.values()) and len(IDs) == T*T:
                            return
                        else:
                            IDs[c] = 0
                    else:
                        pass
                        # console_log("[Not alignable]")
        # If first ID, cycle through and rotate each tile
        else:
            for ID in get_corners():
                for i, tile in enumerate(get_iterations(tiles[ID])):
                    console_log("Tile #{} Iteration #{}\n{}".format(ID, i, tile[:10]))
                    IDs[c] = ID
                    grid[c] = tile
                    solve(get_next_coord(c))
                    if all(IDs.values()) and len(IDs) == T*T:
                        console_log("Grid filled succesfully")
                        return
                    else:
                        IDs[c] = 0

with open("input/day20.txt") as file:
    tiles = {}
    sides = {}
    for t in file.read()[:-1].split("\n\n"):
        ID = int(t[5:9])
        tile = t[11:]
        tiles[ID] = t[11:]
        sides[ID] = get_sides(tile)

part1 = prod(get_corners())

M = len(t.splitlines()[1])
T = int(sqrt(len(tiles)))

grid = defaultdict(str)
IDs = defaultdict(int)

solve((0,0))

# Printing results
print("Answer to AoC day 20 part 1 is: {}".format(part1))
