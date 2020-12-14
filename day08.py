# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 19:16:48 2020

@author: Andreas J. P.
"""

with open("input/day08.txt") as file:
    program = map(lambda s: s.split(' '), file.read().split('\n')[:-1])
    program = list(map(lambda i: (i[0], int(i[1])), program))


def step(program, pc, acc, visited):
    op, arg = program[pc]
    visited.add(pc)
    if op == "nop":
        pc += 1
    elif op == "acc":
        acc += arg
        pc += 1
    elif op == "jmp":
        pc += arg
    return pc, acc, visited


# Runs until a PC is encountered twice or the PC goes out of bounds.
def run(program):
    visited = set()
    acc = pc = 0
    while pc not in visited and pc < len(program):
        pc, acc, visited = step(program, pc, acc, visited)
    return pc, acc, visited


def part1():
    pc, acc, visited = run(program)
    return acc


def part2():
    replacement = {"nop": "jmp", "jmp": "nop"} 
    for i, (op, arg) in enumerate(program):
        # Only run again when a replacement can be made (when op != 'acc')
        if op != "acc":
            i_program = program.copy()
            i_program[i] = (replacement[op], arg)
            pc, acc, visited = run(i_program)
            if pc == len(program):
                return acc


# Printing results
print("Answer to AoC day 8 part 1 is: {}".format(part1()))
print("Answer to AoC day 8 part 2 is: {}".format(part2()))
