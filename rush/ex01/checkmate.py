from check_invalid_board import *

PIECES ={"R","Q","P","B"}

def line_attack(px, py, size, directions, board):
    pos = []
    for dx, dy in directions:
        for i in range(1, size):
            x = px + dx * i
            y = py + dy * i

            if not (0 <= x < size and 0 <= y < size):
                break

            pos.append((x, y))

            if board[y][x] in PIECES:
                break

    return set(pos)
#. . 2 . .
#. . 1 . .      (0, 1)
#2 1 R 1 2 (-1, 0) R (1, 0)
#. . 1 . .      (0, -1)
#. . 2 . .

#2 . . . 2
#. 1 . 1 . (-1, -1) (1, 1)
#. . B . .         B
#. 1 . 1 . (-1, 1)  (1, -1)
#2 . . . 2
def pawn(px: int, py: int):
    return {(px-1, py-1), (px+1, py-1)}
# X . X
# . P .
# . . .


def rook(px, py, size, board):
    return line_attack(
        px, py, size,
        [(0, -1), (-1, 0), (0, 1), (1, 0)],
        board
    )

def bishop(px, py, size, board):
    return line_attack(
        px, py, size,
        [(-1, -1), (1, 1), (-1, 1), (1, -1)],
        board
    )

def queen(px, py, size, board):
    return rook(px, py, size, board) | bishop(px, py, size, board)

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
        for x, value in enumerate(row):
            if value == "R":
                attacks |= rook(x, y, size, matrix)
            if value == "P":
                attacks |= pawn(x, y)
            if value == "B":
                attacks |= bishop(x, y, size, matrix)
            if value == "Q":
                attacks |= queen(x, y, size, matrix)
            if value == "K":
                king_pos = (x, y)
    print("Success" if king_pos in attacks else "Fail")