from csp import CSP, Constraint
from typing import Dict, List, Optional


class QueensConstraint(Constraint[int, int]):

    def __init__(self, columns: List[int]) -> None:
        super().__init__(columns)
        self.columns: List[int] = columns


    def satisfied(self, assignment: Dict[int, int]) -> bool:
        #q1c column of queen 1, q1r row of queen 1
        for q1c, q1r in assignment.items():
            for q2c in range(q1c + 1, len(self.columns) + 1):
                if q2c in assignment:
                    q2r: int = assignment[q2c]
                    if q1r == q2r: 
                        return False
                    if abs(q1r - q2r) == abs(q1c - q2c): #same diagonal
                        return False
        return True


from typing import Dict, List


if __name__ == '__main__':
    columns: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    rows: Dict[int, List[int]] = {}

    for column in columns:
        rows[column] = [1, 2, 3, 4, 5, 6, 7, 8]

    csp: CSP[int, int] = CSP(columns, rows)
    csp.add_contraint(QueensConstraint(columns))
    solution: Optional[Dict[int, int]] = csp.backtracking_search()

    if solution is None:
        print('No solution found!')
    else:
        print(solution)


