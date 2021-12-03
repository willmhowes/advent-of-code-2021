# Day 02.2 - Advent of Code
# Author: Will Howes
# Goal: Calculate the horizontal position and depth you would
#       have after following the planned course. What do you
#       get if you multiply your final horizontal position by
#       your final depth?

def giveInput():
    with open('puzzleinput02.txt', 'r') as file:
        return [x[0:-1] for x in file.readlines()]

def calcMultiple(ls):
    h,d,a = 0,0,0
    for c in ls:
        if c[0] == 'd': a+=int(c[-1])
        elif c[0] == 'u': a-=int(c[-1])
        elif c[0] == 'f':
            h+=int(c[-1])
            d+=int(c[-1])*a
    return h*d

if __name__ == "__main__":
    ls = giveInput()
    print(calcMultiple(ls))
