# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 22:12:37 2022

@author: Andreas J. P.
"""

import numpy as np

with open("input/day22.txt") as file:
    players = file.read()[:-1].split("\n\n")
    players = list(map(lambda s: s.split(":\n")[1], players))
    players = list(map(lambda s: s.split("\n"), players))
    players = [list(map(lambda i: int(i), k)) for k in players]

def play(decks, recursive):
    hands = set()
    while all([len(d) for d in decks]):
        if str(decks) in hands:
            # Forgot to return here which needed a lot of debugging :(
            return 0, decks
        else:
            hands.add(str(decks))
            if (recursive and 
                    len(decks[0]) >= decks[0][0] + 1 and
                    len(decks[1]) >= decks[1][0] + 1):
                copy = [d.copy() for d in decks]
                copy[0] = copy[0][1:copy[0][0] + 1]
                copy[1] = copy[1][1:copy[1][0] + 1]
                winner, _ = play(copy, True)
            else:
                winner = decks[0][0] < decks[1][0]
        decks[winner].append(decks[winner].pop(0))
        decks[winner].append(decks[not winner].pop(0))
    winner = np.argmax([len(d) for d in decks]) 
    return winner, decks[winner]

def get_score(deck):
    return np.sum(deck * np.flip(np.arange(1, len(deck) + 1)))

winner, deck = play([p.copy() for p in players], False)
part1 = get_score(deck)

winner, deck = play([p.copy() for p in players], True)
part2 = get_score(deck)

# Printing results
print("Answer to AoC day 22 part 1 is: {}".format(part1))
print("Answer to AoC day 22 part 2 is: {}".format(part2))
