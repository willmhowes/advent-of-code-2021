# Day 05.2 - Advent of Code
# Author: Will Howes
# Goal: Consider all of the lines. At how many
#       points do at least two lines overlap?

import sys

MAX_LENGTH = 1000

def giveInput():
    # optional command line argument for txt file
    if len(sys.argv) == 2: loc = sys.argv[1]
    else:                  loc = 'puzzleinput05.txt'

    with open(loc, 'r') as file:
        ls = list()
        l = file.readline().rstrip()
        while l != '':
            left, right = l.split(' -> ')
            left0, left1 = [int(x) for x in left.split(',')]
            right0, right1 = [int(x) for x in right.split(',')]
            orientation = 2 # assume diagonal
            if left0 == right0:
                orientation = 0 # horizontal
            elif left1 == right1:
                orientation = 1 # vertical
            ls.append([left0, left1, right0, right1, orientation])
            l = file.readline().rstrip()
        return ls

def countOverlaps(ls):
    markedOnce, markedMult = set(), set()
    for l in ls:
        # compute line direction
        left0, left1, right0, right1, d = l
        dx,dy = 0,0
        if right0 > left0: dy = 1
        else:              dy = -1
        if right1 > left1: dx = 1
        else:              dx = -1

        c, r = left0, left1 # index for tracking position of line

        # diagonal line
        if d == 2:
            while c != right0+dy:
                if (r,c) in markedOnce: markedMult.add((r,c))
                else:                   markedOnce.add((r,c))
                c+=dy # increment column index
                r+=dx # increment row index

        # vertical line
        elif d == 1:
            while c != right0+dy:
                if (r,c) in markedOnce: markedMult.add((r,c))
                else:                   markedOnce.add((r,c))
                c+=dy # increment column index

        # horizontal line
        else:
            while r != right1+dx:
                if (r,c) in markedOnce: markedMult.add((r,c))
                else:                   markedOnce.add((r,c))
                r+=dx # increment row index

    return len(markedMult)

def main():
    ls = giveInput()
    ct = countOverlaps(ls)
    print(ct)

if __name__ == "__main__":
    main()
