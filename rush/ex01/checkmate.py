from check_invalid_board import *

def pawn(px: int, py: int, size: int):
    return {(px-1, py-1), (px+1, py-1)}

def bishop(px: int, py: int, size: int):
    pos = []
    for i in range(1, size):
        pos.extend([(px-i,py-i),(px+i,py+i),(px-i,py+i),(px+i,py-i)])
    return set(pos)

def rook(px: int, py: int, size: int):
    pos = []
    for i in range(1, size):
        pos.extend([(px,py-i),(px-i,py),(px,py+i),(px+i,py)])
    return set(pos)

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
        #0 ['R', '.', '.', '.']
        #1 ['.', 'K', '.', '.']
        #2 ['.', '.', 'P', '.']
        #3 ['.', '.', '.', '.']
        print(y, row)
        for x, value in enumerate(row):
            #0 R, 1 ., 2 . ,3 .
            print(x, value)
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
        print(attacks)
    print("Success" if king_pos in attacks else "Fail")

