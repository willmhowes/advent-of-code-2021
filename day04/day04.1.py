# Day 04.1 - Advent of Code
# Author: Will Howes
# Goal: To guarantee victory against the giant squid, figure
#       out which board will win first. What will your final
#       score be if you choose that board?

def giveInput():
    with open('puzzleinput04.txt', 'r') as file:
        l1 = file.readline().rstrip().split(',')
        file.readline() # remove extra line
        ls = file.readlines()

        i = 0
        boards = list()
        while i < len(ls):
            board = list()
            while i % 6 != 5:
                board.append(ls[i].split())
                i+=1
            boards.append(board)
            i+=1

        return l1, boards

def markBoard(board, n):
    i,j = 0,0
    while i < len(board):
        while j < len(board[0]):
            if board[i][j] == n:
                board[i][j] = 'x'
            j+=1
        i+=1
        j=0


def hasBingo(board):
    # check horizontal
    i,j = 0,0
    while i < len(board) and j < len(board[0]):
        if board[i][j] != 'x':
            i+=1
            j=0
        else:
            j+=1
            if j == len(board[0]):
                return True

    # check vertical
    i,j = 0,0
    while i < len(board) and j < len(board[0]):
        if board[i][j] != 'x':
            j+=1
            i=0
        else:
            i+=1
            if i == len(board):
                return True

    return False

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
