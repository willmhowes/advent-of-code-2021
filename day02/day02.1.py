# Day 02.1 - Advent of Code
# Author: Will Howes
# Goal: Calculate the horizontal position and depth you would
#       have after following the planned course. What do you
#       get if you multiply your final horizontal position by
#       your final depth?

def giveInput():
    with open('puzzleinput02.txt', 'r') as file:
        return [x[0:-1] for x in file.readlines()]

def calcMultiple(ls):
    h = 0
    d = 0
    for c in ls:
        if c[0] == 'f': h+=int(c[-1])
        elif c[0] == 'd': d+=int(c[-1])
        elif c[0] == 'u': d-=int(c[-1])
    return h*d

if __name__ == "__main__":
    ls = giveInput()
    print(calcMultiple(ls))
