from rush.ex01.check_invalid_board import *

def oversize(pos, size: int):
    return set([i for i in pos if i[0] >= 0 and i[1] >= 0 and i[0] < size and i[1] < size])

def pawn(px: int, py: int, size: int):
    return oversize([(px-1, py-1), (px+1, py-1)], size)

def bishop(px: int, py: int, size: int):
    pos = []
    for i in range(1, size):
        pos.extend([(px-i,py-i),(px+i,py+i),(px-i,py+i),(px+i,py-i)])
    return oversize(set(pos), size)

def rook(px: int, py: int, size: int):
    pos = []
    for i in range(1, size):
        pos.extend([(px,py-i),(px-i,py),(px,py+i),(px+i,py)])
    return oversize(set(pos), size)

def queen(px: int, py: int, size: int):
    return rook(px, py, size) | bishop(px,py, size)

def checkmate(board: str):
    invalid, error_message = check_invalid_board(board)
    if invalid:
        return print(error_message)

    matrix = [list(i.strip()) for i in board.splitlines()]
    size = len(matrix)
    attacks = set()
    for y, row in enumerate(matrix):
        for x, value in enumerate(row):
            if value == "R":
                attacks |= rook(x, y, size)
            if value == "P": 
                attacks |= pawn(x, y, size)
            if value == "B":
                attacks |= bishop(x, y, size)
            if value == "Q":
                attacks |= queen(x, y, size)
            if value == "K":
                king_pos = (x, y)
    print("Success" if king_pos in attacks else "Fail")

