import math
import itertools
import scraper


def solve(board):
    n = len(board[0])

    if math.sqrt(n) % 1 != 0:
        raise ValueError("Board is invalid")
    else:
        side = int(math.sqrt(n))

    # we generate a list of indices to be used as keys in a dictionary
    # each pair of indices represents a box in the sudoku
    indices = []
    for x in range(n):
        indices.extend([(x, i) for i in range(n)])

    # we create a dictionary that stores all the possible values of each box in the sudoku
    vals = {}
    for index in indices:
        x, y = index
        if board[x][y] == 0:
            vals[index] = {x for x in range(1, n + 1)}
        else:
            vals[index] = {board[x][y]}

    rcb = itertools.cycle(['row', 'column', 'block'])

    res = [vals, board]
    # performs the layer function until the sudoku is completed
    while is_unfinished(res[1]):
        # in each iteration, res is replaced with the updated dictionary returned from the layer function.
        # board is replaced with the updated board.
        res = layer(n, side, res[0], res[1], next(rcb))

    return res[1]


def layer(n: int, side: int, vals, board, rcb: str):
    # each layer will narrow down the possible values for each box

    # each time the function is called, we either iterate through the rows, columns, or blocks of the sudoku
    if rcb == 'row':
        groups = board
    elif rcb == 'column':
        groups = list(zip(*board))
    else:
        groups = [[board[x + a][y + b] for a in range(side) for b in range(side)]
                  for x in range(0, n, side) for y in range(0, n, side)]

    # iterates through each row, column, or block and narrows down possible
    # values for each box based on the values already present in that group.
    for i, group in enumerate(groups):
        missing = {x for x in range(1, n + 1) if x not in group}
        unknown = [x for x in range(n) if group[x] == 0]
        for x in unknown:
            if rcb == 'row':
                vals[(i, x)] = missing & vals[(i, x)]
            elif rcb == 'column':
                vals[(x, i)] = missing & vals[(x, i)]
            else:
                r = (side * (i // side)) + (x // side)
                c = (side * (i % side)) + (x % side)
                vals[(r, c)] = missing & vals[(r, c)]

    # if there is only one possible value for the box, append that value to the updated board.
    # if there are still multiple possible values, append 0 because that value is still unknown.
    updated_board = [[max(vals[(x, i)]) if len(vals[(x, i)]) == 1 else 0 for i in range(n)] for x in range(n)]
    return vals, updated_board


def is_unfinished(board) -> bool:
    # if there is a 0 on the board, the sudoku is unfinished.
    for row in board:
        if 0 in row:
            return True
    return False

