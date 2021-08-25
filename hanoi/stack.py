from typing import TypeVar, Generic, List
T = TypeVar('T')

class Stack(Generic[T]):
    
    def __init__(self) -> None:
        self.__container: List[T] = []

    def push(self, item: T)-> None:
        self.__container.append(item)

    def pop(self) -> T:
        return self.__container.pop()

    def __repr__(self) -> str:
        return repr(self.__container)
