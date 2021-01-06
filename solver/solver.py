import math
import itertools


def solve(board):
    n = len(board[0])

    if math.sqrt(n) % 1 != 0:
        raise ValueError("Board is invalid")
    else:
        side = int(math.sqrt(n))

    # we create a dictionary with every unknown box and their
    # corresponding possible values (starts as any number from 1 to n)
    vals = {}
    for i in range(n):
        for x in range(n):
            if board[i][x] == 0:
                vals[(i, x)] = {x for x in range(1, n + 1)}

    rcb = itertools.cycle(["row", "column", "block"])

    res = [vals, board]
    # performs the layer function until there are no more unknown values (the length of the dictionary is 0)
    while res[0]:
        # in each iteration, vals is replaced with the updated dictionary returned from the layer function.
        # board is replaced with the updated board.
        res = layer(n, side, res[0], res[1], next(rcb))

    return res[1]


def layer(n: int, side: int, vals, board, rcb: str):
    # each layer will narrow down the possible values for each box

    # each time the function is called, we either iterate through the rows, columns, or blocks of the sudoku
    if rcb == "row":
        groups = board
    elif rcb == "column":
        groups = list(zip(*board))
    else:
        groups = [
            [board[x + a][y + b] for a in range(side) for b in range(side)]
            for x in range(0, n, side)
            for y in range(0, n, side)
        ]

    # iterates through each row, column, or block and narrows down possible
    # values for each box based on the values already present in that group.
    # if we have narrowed it down to only one possible value in a box, modify the board
    # to express that and remove the box from the dictionary of unknowns
    for i, group in enumerate(groups):
        missing = {x for x in range(1, n + 1) if x not in group}
        unknown = [x for x in range(n) if group[x] == 0]
        for x in unknown:
            if rcb == "row":
                vals[(i, x)] &= missing
                if len(vals[(i, x)]) == 1:
                    board[i][x] = vals.pop((i, x)).pop()
            elif rcb == "column":
                vals[(x, i)] &= missing
                if len(vals[(x, i)]) == 1:
                    board[x][i] = vals.pop((x, i)).pop()
            else:
                row = (side * (i // side)) + (x // side)
                column = (side * (i % side)) + (x % side)
                vals[(row, column)] &= missing
                if len(vals[(row, column)]) == 1:
                    board[row][column] = vals.pop((row, column)).pop()

    return vals, board
