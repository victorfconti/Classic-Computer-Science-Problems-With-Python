from __future__ import annotations
from priority_queue import PriorityQueue
from queue import Queue
from node import Node
from typing import TypeVar, Iterable, Sequence, Generic, List, Callable, Set, Deque, Dict, Any, Optional, Protocol
from heapq import heappush, heappop
from stack import Stack


T = TypeVar('T')

def linear_contains(iterable: Iterable[T], key: T) -> bool:
    for item in iterable:
        if item == key:
            return True
    return False


C = TypeVar('C', bound="Comparable")

class Comparable(Protocol):

    def __eq__(self, o: object) -> bool:
        ...

    def __lt__(self: C, other: Any) -> bool:
        ...

    def __gt__(self: C, other: C) -> bool:
        return (not self < other) and self != other

    def __le__(self: C, other: C) -> bool:
        return self < other or self == other

    def __ge__(self: C, other: C) -> bool:
        return not self < other
    
def binary_contains(sequence: Sequence[C], key: C) -> bool:
    low: int = 0
    high: int = len(sequence) - 1

    while low <= high:
        mid: int = (low + high) // 2
        if sequence[mid] < key:
            low = mid + 1
        elif sequence[mid] > key:
            high = mid - 1
        else:
            return True
    return False


def dfs(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]]) -> Optional[Node[T]]:
    frontier: Stack[Node[T]] = Stack()
    frontier.push(Node(initial, None))
    explored: Set[T] = {initial}

    while not frontier.empty:
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state
        
        if goal_test(current_state):
            return current_node

        for child in successors(current_state):
            if child in explored:
                continue
            
            explored.add(child)
            frontier.push(Node(child, current_node))
    
    return None


def bfs(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]]) -> Optional[Node[T]]:
    frontier: Queue[Node[T]] = Queue()
    frontier.push(Node(initial, None))
    explored: Set[T] = {initial}

    while not frontier.empty:
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state

        if goal_test(current_state):
            return current_node

        for child in successors(current_state):
            if child in explored:
                continue
            
            explored.add(child)
            frontier.push(Node(child, current_node))


def astar(initial: T, goal_test: Callable[[T], bool], sucessors: Callable[[T], List[T]], heuristic: Callable[[T], float]) -> Optional[Node[T]]:
    frontier: PriorityQueue[Node[T]] = PriorityQueue()
    frontier.push(Node(initial, None, 0.0, heuristic(initial)))
    explored: Dict[T, float] = {initial: 0.0}

    while not frontier.empty:
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state

        if goal_test(current_state):
            return current_node

        for chield in sucessors(current_state):
            new_cost: float = current_node.cost + 1

            if chield not in explored or explored[chield] > new_cost:
                explored[chield] = new_cost
                frontier.push(Node(chield, current_node, new_cost, heuristic(chield)))
    return None

if __name__ == '__main__':
    print(linear_contains([1,2,3,4], 5))
    print(linear_contains([1,2,3,4], 3))

    print(binary_contains([1,2,3,4,5], 3))
    print(binary_contains([1,2,3,4,5], 7))

    print(binary_contains(["Adan", "Kleiton", "Zhorg"], "Kleiton"))
    print(binary_contains(["Adan", "Kleiton", "Zhorg"], "Kleithon"))

