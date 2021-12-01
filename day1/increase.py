# Day 01.1 - Advent of Code
# Author: Will Howes
# Goal: Count the number of times a depth measurement increases
#       from the previous measurement.

from puzzleinput import ls

i,ct = 1,0
while i < len(ls):
    if ls[i] > ls[i-1]: ct+=1
    i+=1

print(ct)
