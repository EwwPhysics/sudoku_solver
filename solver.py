import heapq
import itertools
import typing as t

class PriorityQueue:
    """
    Custom priority queue to add additional functionality
    to python's heapq
    """
    def __init__(self) -> None:
        self.queue = []
        self.counter = itertools.count()
        self.entries = {}

    def push(self, item, priority: int) -> None:
        """
        Add an item to the queue with given priority.
        If the item is already present in the queue,
        update the present item with the new priority if
        it is lower
        """
        if item in self.entries:
            entry = self.entries[item]
            entry[0] = min(entry[0], priority)
        else:
            entry = [priority, next(self.counter), item]
            self.entries[item] = entry
            heapq.heappush(self.queue, entry)

    def pop(self):
        _, _, item = heapq.heappop(self.queue)
        del self.entries[item]
        return item




class Solver:
    def __init__(self, puzzle) -> None:
        self.puzzle = puzzle
        self.queue = PriorityQueue()
