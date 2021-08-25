
def calculator_pi(n_terms: int) -> float:
    cdef:
        float numerator = 4.0
        float denominator = 1.0
        float operation = 1.0
        float pi = 0.0

    for _ in range(n_terms):
        pi += operation * (numerator / denominator)
        denominator += 2
        operation *= -1
    
    return pi
