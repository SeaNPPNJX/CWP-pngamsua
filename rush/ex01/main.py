from checkmate import checkmate

def main():
    board = """\
R...
.K..
..K.
....\
"""

# board = """\
# ..
# .K\
# """

    try:
        checkmate(board)
        return
    except Exception as e:
        print(e)
        return

if __name__ == "__main__":
    main()
