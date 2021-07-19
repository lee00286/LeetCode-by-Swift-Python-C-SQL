class Solution:
    def countTriples(self, n: int) -> int:
        if n == 1:
            return 0

        # List of squares
        squares = []
        for i in range(2, n + 1):
            squares.append(i ** 2)

        # Count square sum triples
        count = 0
        for a in range(1, n - 1):
            for b in range(a + 1, n):
                if a ** 2 + b ** 2 in squares:
                    count += 2

        return count
