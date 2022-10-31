# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 12:23:35 2022

@author: oluwo

"""

# A simple rock, papers, scissors game

def rock_p_s(p1, p2):
    if p1 == p2:
        return 'Draw'
    while p1 == 'scissors':
        if p2 == 'paper':
            return 'Player1 won'
        else:
            return 'Player2 won'
    while p1 == 'paper':
        if p2 == 'scissors':
            return 'Player2 won'
        else:
            return 'Player1 won'
    while p1 == 'rock':
        if p2 == 'scissors':
            return 'Player1 won'
        else:
            return 'Player2 won'
        
print(rock_p_s('scissors', 'paper'))