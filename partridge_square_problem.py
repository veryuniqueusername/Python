# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 22:43:55 2025

@author: Emilia
"""

n = 8
sq_len = (n * (n + 1) // 2)


def print_board(board, highlighted_index):
    formatted_board = []
    for i in range(len(board)):
        if i == highlighted_index:
            formatted_board.append("X ")
        elif board[i]:
            formatted_board.append("■ ")
        else:
            formatted_board.append("□ ")
        if (i + 1) % sq_len == 0:
            formatted_board.append("\n")
    print("".join(formatted_board))


def space_available(board, position_index, size):
    if (position_index % sq_len) + size > sq_len:
        # print("Too large for board horisontally")
        return False
    if (position_index // sq_len) + size > sq_len:
        # print("Too large for board vertically")
        return False
    for i in range(position_index + 1, position_index + size):
        if board[i]:
            # print("Too large, overlapping")
            return False
    return True


def fill_space(board, position_index, size):
    new_board = board.copy()
    for i in range(size):
        for j in range(size):
            new_board[position_index + i + j * sq_len] = True
    return new_board


def board_from_size_sequence(size_sequence):
    board = [False] * sq_len ** 2
    index = 0
    for position_index in range(sq_len ** 2):
        if board[position_index]:
            continue
        board = fill_space(board, position_index, size_sequence[index])
        index += 1
    return board


solution = [8, 8, 8, 8, 4, 4, 8, 8, 8, 5, 7, 5, 7, 8, 4, 5, 7, 5, 4, 5, 7, 6, 6, 6, 6, 2, 3, 2, 1, 7, 7, 7, 6, 6, 3, 3]

print_board(board_from_size_sequence(solution), -1)


def main():
    attempt = 0
    size_order = []
    position_order = []
    boards = [[False] * sq_len ** 2]

    try:
        position_index = 0
        last_size = n + 1
        while True:
            # print_board(boards[-1], position_index)
            if boards[-1][position_index]:
                # print("Position {} already filled".format(position_index))
                position_index += 1
                continue
            # print("Position {} empty, trying from size".format(position_index), last_size - 1)
            if last_size > 1:
                for size in range(last_size - 1, 0, -1):
                    # print("Testing size", size)
                    if size_order.count(size) == size:
                        # print("Used up all", size)
                        if size > 1:
                            continue
                    elif space_available(boards[-1], position_index, size):
                        # print("Space for size", size)
                        size_order.append(size)
                        position_order.append(position_index)
                        boards.append(fill_space(boards[-1], position_index, size))
                        attempt += 1
                        # print("Attempt number", attempt)
                        # print(size_order, ":")
                        # print_board(boards[-1], position_index)
                        last_size = n + 1
                        if size_order == solution[0:len(size_order)]:
                            print("Attempt number", attempt)
                            print(size_order, ":")
                            print_board(boards[-1], position_index)
                            print("Correct path")
                        if len(size_order) == sq_len:
                            print(size_order)
                            print("Board found")
                            raise StopIteration
                        break
                    # print("No space for size", size, "at", position_index)
                    # print_board(boards[-1], position_index)
                    if size > 1:
                        continue
                    # print("Invalid structure, backtracking to")
                    last_size = size_order.pop()
                    position_index = position_order.pop()
                    boards.pop()
                    # print(size_order, ":")
                    # print_board(boards[-1], position_index)
            else:
                # print("All 1s are used up! Impossible continuation, backtracking to")
                last_size = size_order.pop()
                position_index = position_order.pop()
                boards.pop()
                # print(size_order, ":")
                # print_board(boards[-1], position_index)

    except Exception as e:
        print(e)
        print("Stopped")


main()
