from checkmate import checkmate

def main():
    board = """\
RK..
R...
....
....\
"""

#     board = """\
# ..
# .K\
# """
    # print([1,2,3][-1])
    # print([1,2,3][4])
    try:
        checkmate(board)
        return
    except Exception as e:
        print(e)
        return
    
if __name__ == "__main__":
    main()
