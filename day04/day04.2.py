# Day 04.2 - Advent of Code
# Author: Will Howes
# Goal: Figure out which board will win last. Once it wins,
#       what would its final score be?

from bingo import *

def finishGame(nums, board):
    for n in nums:
        markBoard(board, n)
        if hasBingo(board):
            return n, board

def findLastWinner(nums, boards):
    winners = 0
    for i in range(len(nums)):
        for board in boards:
            if board[0][0] != 'b':
                markBoard(board, nums[i])
                if hasBingo(board):
                    board[0][0]='b'
                    winners+=1
        if winners == len(boards)-1:
            for board in boards:
                if board[0][0] != 'b':
                    return finishGame(nums[i+1:], board)

def main():
    nums, boards = giveInput()
    n, board = findLastWinner(nums, boards)
    final = calcFinalScore(n,board)
    print(final)

if __name__ == "__main__":
    main()
