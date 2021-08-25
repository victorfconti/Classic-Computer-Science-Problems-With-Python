import cython
import pi

def calculator_pi(n_terms: int) -> float:
    numerator: float = 4.0
    denominator: float = 1.0
    operation: float = 1.0
    pi: float = 0.0

    for _ in range(n_terms):
        pi += operation * (numerator / denominator)
        denominator += 2
        operation *= -1
    
    return pi


if __name__ == "__main__":
    print(calculator_pi(100000))
    print(pi.calculator_pi(100000))
