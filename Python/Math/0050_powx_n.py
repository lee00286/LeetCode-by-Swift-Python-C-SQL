class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Special case
        if n == 0:
            return 1
        # Negative exponent
        if n < 0:
            return self.myPow(1 / x, abs(n))
        # Odd exponent
        if n % 2 != 0:
            return x * self.myPow(x, n - 1)
        # Even exponent
        return self.myPow(x * x, n // 2)
