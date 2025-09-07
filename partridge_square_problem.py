# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 22:43:55 2025

@author: Emilia
"""

n = 5
sq_len = (n*(n+1)//2)
size_order = []
position_order = []
boards = [[False] * sq_len**2]


def print_board(board, highlighted_index):
    formatted_board = []
    for i in range(len(board)):
        if i == highlighted_index:
            formatted_board.append("X")
        elif board[i]:
            formatted_board.append("■")
        else:
            formatted_board.append("□")
        if (i+1) % sq_len == 0:
            formatted_board.append("\n")
    print("".join(formatted_board))


def space_available(board, position_index, size):
    if (position_index % sq_len) + size > sq_len:
        print("Too large for board horisontally")
        return False
    if (position_index // sq_len) + size > sq_len:
        print("Too large for board vertically")
        return False
    for i in range(position_index + 1, position_index + size):
        if board[i]:
            print("Too large, overlapping")
            return False
    return True


def fill_space(board, position_index, size):
    new_board = board.copy()
    for i in range(size):
        for j in range(size):
            new_board[position_index + i + j*sq_len] = True
    return new_board


try:
    i = 0
    last_size = n+1
    while True:
        if boards[-1][i]:
            continue
        for size in range(last_size - 1, 0, -1):
            if size == 0:
                print("Size is 0")
                raise StopIteration
            print("Testing size", size)
            if size_order.count(size) == size:
                print("Used up all", size)
                if size > 1:
                    continue
            elif space_available(boards[-1], i, size):
                print("Space for size", size)
                size_order.append(size)
                position_order.append(i)
                boards.append(fill_space(boards[-1], i, size))
                print(size_order, ":")
                print_board(boards[-1], i)
                last_size = n+1
                break
            print("No space for size", size, "at", i)
            print_board(boards[-1], i)
            if size > 1:
                continue
            print("Invalid structure, backtracking to")
            last_size = size_order.pop()
            boards.pop()
            print_board(boards[-1], i)

except Exception as e:
    print(e)
    print("Stopped")
