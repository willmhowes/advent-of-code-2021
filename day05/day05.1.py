# Day 05.1 - Advent of Code
# Author: Will Howes
# Goal: Consider only horizontal and vertical lines.
#       At how many points do at least two lines overlap?

import sys

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
            if left0 == right0:
                if left1 > right1:
                    left1, right1 = right1, left1
                ls.append([left0, left1, right0, right1, 0])
            elif left1 == right1:
                if left0 > right0:
                    left0, right0 = right0, left0
                ls.append([left0, left1, right0, right1, 1])
            l = file.readline().rstrip()
        return ls

def fillGrid(ls):
    grid = [[0 for x in range(1000)] for x in range(1000)]
    for l in ls:
        if l[4]:
            i = l[0]
            while i < l[2]+1:
                grid[l[1]][i] += 1
                i+=1
        else:
            i = l[1]
            while i < l[3]+1:
                grid[i][l[0]] += 1
                i+=1
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
