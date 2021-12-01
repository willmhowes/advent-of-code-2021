# Day 01.2 - Advent of Code
# Author: Will Howes
# Goal: Consider sums of a three-measurement sliding window.
#       Count the number of times the sum of measurements in
#       this sliding window increases from the previous sum

from puzzleinput import ls

i,ct = 2,0
while i < len(ls)-1:
    # can simplify each window to the unique term
    # between neighboring windows
    if ls[i+1] > ls[i-2]: ct+=1
    i+=1

print(ct)
