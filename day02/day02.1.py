# Day 02.1 - Advent of Code
# Author: Will Howes
# Goal: Calculate the horizontal position and depth you would
#       have after following the planned course. What do you
#       get if you multiply your final horizontal position by
#       your final depth?

import re

def giveInput():
    with open('puzzleinput02.txt', 'r') as file:
        p = re.compile(r'(\w)\w+ (\d+)')
        return re.findall(p, file.read())

def calcMultiple(ls):
    h,d = 0,0
    for c in ls:
        if c[0] == 'f': h+=int(c[1])
        elif c[0] == 'd': d+=int(c[1])
        elif c[0] == 'u': d-=int(c[11])
    return h*d

if __name__ == "__main__":
    ls = giveInput()
    print(calcMultiple(ls))
