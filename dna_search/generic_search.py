from __future__ import annotations
from typing import TypeVar, Iterable, Sequence, Generic, List, Callable, Set, Deque, Dict, Any, Optional, Protocol
from heapq import heappush, heappop

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

if __name__ == '__main__':
    print(linear_contains([1,2,3,4], 5))
    print(linear_contains([1,2,3,4], 3))

    print(binary_contains([1,2,3,4,5], 3))
    print(binary_contains([1,2,3,4,5], 7))

    print(binary_contains(["Adan", "Kleiton", "Zhorg"], "Kleiton"))
    print(binary_contains(["Adan", "Kleiton", "Zhorg"], "Kleithon"))

