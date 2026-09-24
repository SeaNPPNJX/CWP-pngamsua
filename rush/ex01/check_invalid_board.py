
def check_invalid_board(board: str):
    if board.count("K") != 1:
        return True, "Error: The numbers of king does not meet the conditions."
    
    matrix = [list(i.strip()) for i in board.splitlines()]
    for i in matrix:
        if len(i) != len(matrix):
            return True, "Error: The chess does not meet the conditions."

    return False, ""