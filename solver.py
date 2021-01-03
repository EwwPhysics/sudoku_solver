import math
import itertools
import scraper


def solve(board):
    rcb = itertools.cycle(['row', 'column', 'board'])
    n = len(board[0])

    if math.sqrt(n) % 1 != 0:
        return 'Board invalid, try again.'
    else:
        side = int(math.sqrt(n))

    indices = []
    for x in range(n):
        indices.extend([(x, i) for i in range(n)])

    vals = {}
    for index in indices:
        if board[index[0]][index[1]] == 0:
            vals[index] = {x for x in range(1, n + 1)}
        else:
            vals[index] = {board[index[0]][index[1]]}

    res = [vals, board]
    while unfinished(res[1]):
        res = layer(n, side, res[0], res[1], next(rcb))

    return res[1]


def layer(n, side, vals, board, rcb):
    if rcb == 'row':
        iterable = board
    elif rcb == 'column':
        iterable = list(zip(*board))
    else:
        iterable = [[board[x + a][y + b] for a in range(side) for b in range(side)]
                    for x in range(0, n, side) for y in range(0, n, side)]

    for i, row in enumerate(iterable):
        missing = {x for x in range(1, n + 1) if x not in row}
        empty = [x for x in range(n) if row[x] == 0]
        for x in empty:
            if rcb == 'row':
                vals[(i, x)] = missing & vals[(i, x)]
            elif rcb == 'column':
                vals[(x, i)] = missing & vals[(x, i)]
            else:
                r = (side * (i // side)) + (x // side)
                c = (side * (i % side)) + (x % side)
                vals[(r, c)] = missing & vals[(r, c)]

    b = [[max(vals[(x, i)]) if len(vals[(x, i)]) == 1 else 0 for i in range(n)] for x in range(n)]
    return vals, b


def unfinished(board):
    for row in board:
        if 0 in row:
            return True
    return False


a = scraper.get_puzzle('592604')
print(a)
print(solve(a))
