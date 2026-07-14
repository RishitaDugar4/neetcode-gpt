class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        minimizer = init

        for _ in range(iterations):
            derrivative = minimizer * 2
            minimizer = minimizer - (derrivative * learning_rate)

        return round(minimizer, 5)

    