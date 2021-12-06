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

def fillGrid(ls):
    grid = [[0 for x in range(MAX_LENGTH)] for x in range(MAX_LENGTH)]
    for l in ls:
        # compute direction
        left0, left1, right0, right1, d = l
        dx,dy = 0,0
        if right0 > left0: dy = 1
        else:              dy = -1
        if right1 > left1: dx = 1
        else:              dx = -1

        # diagonal line
        if d == 2:
            c, r = left0, left1
            while c != right0+dy:
                grid[r][c] += 1
                c+=dy
                r+=dx

        # vertical line
        elif d == 1:
            c = left0
            while c != right0+dy:
                grid[left1][c] += 1
                c+=dy

        # horizontal line
        else:
            r = left1
            while r != right1+dx:
                grid[r][left0] += 1
                r+=dx

    return grid

def countGridRepeats(grid):
    ct = 0
    for r in grid:
        for c in r:
            if c > 1:
                ct+=1
    return ct

def main():
    ls = giveInput()
    grid = fillGrid(ls)
    count = countGridRepeats(grid)
    print(count)

if __name__ == "__main__":
    main()
