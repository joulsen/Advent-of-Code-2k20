# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 17:23:30 2022

@author: Andreas J. P.
"""

with open("input/day18.txt") as file:
    homework = file.read().replace(" ", "").split('\n')[:-1]
    
def get_postfix(infix, presedence):
    stack = []
    postfix = []
    for char in infix:
        if char == "(":
            postfix += char
        elif char == ")":
            while postfix[-1] != "(":
                stack += postfix.pop()
            postfix.pop()
        elif (char in "*+") and (not presedence):
            try:
                if postfix[-1] in "*+":
                    stack += postfix.pop()
            except IndexError:
                pass
            postfix += char
        elif char == "+":
            try:
                if postfix[-1] == "+":
                    stack += postfix.pop()
            except IndexError:
                pass
            postfix += char
        elif char == "*":
            try:
                if postfix[-1] in "*+":
                    stack += postfix.pop()
            except IndexError:
                pass
            postfix += char
        else:
            stack += char
    while postfix:
        stack += postfix.pop()
    return stack

def evaluate_postfix(postfix):
    stack = []
    for char in postfix:
        if char == "+":
            stack.append(stack.pop() + stack.pop())
        elif char == "*":
            stack.append(stack.pop() * stack.pop())
        else:
            stack.append(int(char))
    return stack[0]

part1 = sum([evaluate_postfix(get_postfix(l, False)) for l in homework])
part2 = sum([evaluate_postfix(get_postfix(l, True)) for l in homework])
# Printing results
print("Answer to AoC day 18 part 1 is: {}".format(part1))
print("Answer to AoC day 18 part 2 is: {}".format(part2))