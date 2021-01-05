import heapq


class PriorityQueue:
    """
    Custom priority queue to add additional functionality
    to python's heapq.
    It is a min heap; an item with a lower priority will be popped
    before an item with a higher priority
    """

    def __init__(self) -> None:
        self.queue = []
        self.entries = {}

    def push(self, item, priority: int) -> None:
        """
        Add an item to the queue with given priority.
        If the item is already in the queue with a higher
        priority, modify the existing item.
        """

        if item in self.entries:
            entry = self.entries[item]
            entry[0] = min(entry[0], priority)
        else:
            entry = [priority, item]
            self.entries[item] = entry
            heapq.heappush(self.queue, entry)

    def pop(self):
        """
        Removes the item with the lowest priority and
        returns an (item, priority) tuple
        """

        priority, item = heapq.heappop(self.queue)
        del self.entries[item]
        return item, priority

    def increment_priority(self, item):
        if entry := self.entries.get(item):
            entry[0] += 1

    def decrement_priority(self, item):
        if entry := self.entries.get(item):
            entry[0] -= 1


    def __len__(self) -> int:
        return len(self.queue)

    def __bool__(self) -> bool:
        return bool(self.queue)

    def __str__(self) -> str:
        return str(self.queue)


class Solver:
    BLOCKS = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
    ]
    FULL = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    def __init__(self, puzzle) -> None:
        self.puzzle = puzzle
        self.queue = PriorityQueue()
        self.solved = False
        self.adj = {}

        for i, row in enumerate(puzzle):
            for j, v in enumerate(row):
                if not v:
                    t = i, j
                    self.queue.push(t, len(self._valid_choices(i, j)))
                    self.adj[t] = {self.puzzle[x][y] for x, y in self._adjacent_squares(i, j)}

    def solve(self) -> None:
        """
        Solves the puzzle in place or does nothing if
        the puzzle is already solved.
        """

        if self.solved:
            return

        (nx, ny), _ = self.queue.pop()
        self._dfs(nx, ny)
        self.solved = True

    def _dfs(self, x, y):
        if len(self.queue) == 0:
            return True

        (nx, ny), priority = self.queue.pop()
        for v in self._valid_choices(x, y):
            self._set_square(x, y, v)

            if self._dfs(nx, ny):
                return True

            self._set_square(x, y, 0)

        self.queue.push((nx, ny), priority)
        return False

    def _set_square(self, x: int, y: int, v: int) -> None:
        self.puzzle[x][y] = v
        if v:
            for item in self.adj[(x, y)]:
                self.queue.decrement_priority(item)
        else:
            for item in self.adj[(x, y)]:
                self.queue.increment_priority(item)


    def _valid_choices(self, x: int, y: int) -> set[int]:
        return Solver.FULL - {self.puzzle[i][j] for i, j in self._adjacent_squares(x, y)}

    def _adjacent_squares(self, x: int, y: int) -> set[tuple[int, int]]:
        xy_squares = set()
        for i in range(9):
            xy_squares.add((i, y))
            xy_squares.add((x, i))

        block_squares = set()
        for i in Solver.BLOCKS:
            for j in i:
                if j == x:
                    row = i
                if j == y:
                    col = i
        for i in row:
            for j in col:
                block_squares.add((i, j))

        all_squares = set.union(xy_squares, block_squares)
        all_squares.remove((x, y))
        return all_squares


