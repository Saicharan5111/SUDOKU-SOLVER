import pyautogui as pg
import time
import numpy as np

def isValid(board, row, col, c):
    for i in range(9):
        if board[i][col] == c:
            return False
        if board[row][i] == c:
            return False
        if board[(row // 3) * 3 + i // 3][(col // 3) * 3 + i % 3] == c:
            return False
    return True


def Print(matrix):
    final = []
    str_fin = []
    for i in range(9):
        final.append(matrix[i])

    for lists in final:
        for num in lists:
            str_fin.append(str(num))

    counter = 0

    for num in str_fin:
        pg.press(num)
        pg.hotkey('right')
        counter += 1
        if counter % 9 == 0:
            pg.hotkey('down')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')


def solve(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for n in range(1, 10):
                    if isValid(board, i, j, n):
                        board[i][j] = n
                        if solve(board):
                            return True
                        else:
                            board[i][j] = 0
                return False
    Print(board)
    input("More?")


grid = []

while True:
    row = list(input('Row: '))
    ints = []

    for n in row:
        ints.append(int(n))
    grid.append(ints)

    if len(grid) == 9:
        break
    print('Row ' + str(len(grid)))

time.sleep(5)

solve(grid)
