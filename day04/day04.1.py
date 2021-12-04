# Day 04.1 - Advent of Code
# Author: Will Howes
# Goal: To guarantee victory against the giant squid, figure
#       out which board will win first. What will your final
#       score be if you choose that board?

from bingo import *

def findWinner(nums, boards):
    for n in nums:
        for board in boards:
            markBoard(board, n)
            if hasBingo(board):
                return n, board

def main():
    nums, boards = giveInput()
    n, board = findWinner(nums, boards)
    final = calcFinalScore(n,board)
    print(final)

if __name__ == "__main__":
    main()
