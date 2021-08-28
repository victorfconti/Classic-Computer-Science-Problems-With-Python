import enum
from generic_search import bfs, dfs
from node import Node, node_to_path
import random
from enum import Enum
from typing import List, NamedTuple, Callable, Optional
from math import sqrt
# from generic_search import dfs, bfs, node_to_path, astar, Node

class Cell(str, Enum):
    EMPTY = ' '
    BLOCKED = 'X'
    START = 'S'
    GOAL = 'G'
    PATH = '*'


class MazeLocation(NamedTuple):
    row: int
    column: int


class Maze:

    def __init__(self, rows: int = 10, columns: int = 10, sparseness: float = 0.2, 
    start: MazeLocation = MazeLocation(0, 0), goal: MazeLocation = MazeLocation(9, 9)) -> None:
        self._rows: int = rows
        self._columns = columns
        self.start: MazeLocation = start
        self.goal: MazeLocation = goal
        #Gera o grid inicial vazio
        self._grid: List[List[Cell]] = [[Cell.EMPTY for c in range(columns)] for r in range(rows)]
        #Preenche o grid
        self._randomly_fill(rows=rows, columns=columns, sparseness=sparseness)
        #Preenche a posição final e a posição inicial
        self._grid[start.row][start.column] = Cell.START
        self._grid[goal.row][goal.column] = Cell.GOAL


    def _randomly_fill(self, rows: int, columns: int, sparseness: float) -> None:
        for row in range(rows):
            for column in range(columns):
                if random.uniform(0, 1.0) < sparseness:
                    self._grid[row][column] = Cell.BLOCKED


    def goal_test(self, ml: MazeLocation) -> bool:
        return ml == self.goal


    def successors(self, ml: MazeLocation) -> List[MazeLocation]:
        locations: List[MazeLocation] = []
        if ml.row + 1 < self._rows and self._grid[ml.row + 1][ml.column] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row + 1, ml.column))
        if ml.row - 1 >= 0 and self._grid[ml.row - 1][ml.column] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row - 1, ml.column))
        if ml.column + 1 < self._columns and self._grid[ml.row][ml.column + 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.column + 1))
        if ml.column - 1 >= 0 and self._grid[ml.row][ml.column - 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.column - 1))
        return locations


    def __str__(self) -> str:
        output: str = ''
        for row in self._grid:
            output += "".join([c.value for c in row]) + '\n'
        return output


    def mark(self, path: List[MazeLocation]) -> None:
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.PATH
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL
    

    def clear(self, path: List[MazeLocation]) -> None:
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.EMPTY
        self._grid[self.start.row][self.start.column] = Cell.EMPTY
        self._grid[self.goal.row][self.goal.column] = Cell.EMPTY


if __name__ == '__main__':
    maze: Maze = Maze()
    print(maze)
    print()

    solution1: Optional[Node[MazeLocation]] = dfs(maze.start, maze.goal_test, maze.successors)
    solution2: Optional[Node[MazeLocation]] = bfs(maze.start, maze.goal_test, maze.successors)

    if solution1 is None:
        print('No solutions found using depth-first search!')
    else:
        path1: List[MazeLocation] = node_to_path(solution1)
        maze.mark(path=path1)
        print(maze)
        maze.clear(path1)


    if solution2 is None:
        print('No solutions found using breadth-first search!')
    else:
        path2: List[MazeLocation] = node_to_path(solution2)
        maze.mark(path=path2)
        print(maze)
        maze.clear(path=path2)
