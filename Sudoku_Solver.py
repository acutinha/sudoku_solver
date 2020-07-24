# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 23:56:42 2020

@author: Akhil
"""

board = [
            [0,2,0,6,0,8,0,0,0],
            [5,8,0,0,0,9,7,0,0],
            [0,0,0,0,4,0,0,0,0],
            [3,7,0,0,0,0,5,0,0],
            [6,0,0,0,0,0,0,0,4],
            [0,0,8,0,0,0,0,1,3],
            [0,0,0,0,2,0,0,0,0],
            [0,0,9,8,0,0,0,3,6],
            [0,0,0,3,0,6,0,9,0]
        ]

def print_board(board):
    ''' board: Sudoku board values passed as a 2-D array
        Function prints each value of the 2D array in a Sudoku board layout
        '''
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-------------------------------")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(board[i][j]," ", end="")
                
def locate_empty(board):
    ''' board: Sudoku board values passed as a 2-D array
        Function loops through the board and returns the location of an empty (0) element
        '''
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col

    return None

def find_correct(board, num, loc):
    ''' board: Sudoku board values passed as a 2-D array
        num: Positive integer value entered into the board
        loc: Location values (x,y) of the empty(0) element
        Function returns False if the input value is repeated in the row, column, or cube. If all Sudoku rules are followed it reutrns True
        '''
    # Check row repetation
    for i in range(len(board[0])):
        if board[loc[0]][i] == num and loc[1] != i:
            return False

    # Check column repetation
    for i in range(len(board)):
        if board[i][loc[1]] == num and loc[0] != i:
            return False

    # Check box repetation
    box_x = loc[1] // 3     #Splits the board into cubes of 3*3
    box_y = loc[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != loc:
                return False

    return True

                
def solve(board):
    find = locate_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if find_correct(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

print("Howdy! Let us solve the Sudoku board:\n")
print_board(board)
print("\nSolving board . . .")
solve(board)
print("\nThe solved board is:\n")
print_board(board)