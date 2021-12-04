# Day 04.1 - Advent of Code
# Author: Will Howes
# Goal: To guarantee victory against the giant squid, figure
#       out which board will win first. What will your final
#       score be if you choose that board?

from bingo import giveInput,markBoard,hasBingo

def bingoOperator(nums, boards):
    for n in nums:
        for board in boards:
            markBoard(board, n)
            if hasBingo(board):
                return board, n

def calcFinalScore(nums, boards):
    board, n = bingoOperator(nums, boards)
    sum = 0
    for row in board:
        for col in row:
            if col != 'x': sum+=int(col)
    return sum*int(n)

if __name__ == "__main__":
    nums, boards = giveInput()
    print(calcFinalScore(nums,boards))
