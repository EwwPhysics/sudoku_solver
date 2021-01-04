import heapq
import itertools

class PriorityQueue:
    """
    Custom priority queue to add additional functionality
    to python's heapq.
    It is a min heap; an item with a lower priority will be popped
    before an item with a higher priority
    """

    def __init__(self) -> None:
        self.queue = []
        self.counter = itertools.count()
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
            entry = [priority, next(self.counter), item]
            self.entries[item] = entry
            heapq.heappush(self.queue, entry)


    def pop(self):
        """
        Removes and returns the item with the lowest prority.
        """

        _, _, item = heapq.heappop(self.queue)
        del self.entries[item]
        return item


    def __len__(self) -> int:
        return len(self.queue)

    def __bool__(self) -> int:
        return bool(self.queue)


class Solver:
    """
    """

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

        for i, row in enumerate(puzzle):
            for j, _ in enumerate(row):
                self.queue.push((i, j), len(self._valid_choices(i, j)))

    def solve(self) -> None:
        """
        Solves the puzzle in place or does nothing if
        the puzzle is already solved.
        """

        if self.solved:
            return

    def _dfs(self, x, y):
        if not self.queue:
            return



    def _valid_choices(self, x: int, y: int) -> set[int]:
        A = set(self.puzzle[x])
        B = {self.puzzle[i][y] for i in range(9)}
        C = set()
        for i in Solver.BLOCKS:
            for j in i:
                if j == x:
                    row = i
                if j == y:
                    col = i
        for i in row:
            for j in col:
                C.add(self.puzzle[i][j])

        return Solver.FULL - A - B - C

