class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if (n <= 0):
            return False
        
        while (n % 3 == 0):
            n = n // 3
        
        return n == 1
    
        """
        # ===== Multiplication
        if (n <= 0):
            return False
        
        num = 1
        while (num < n):
            num = num * 3
        
        return num == n
        """
        """
        # ===== Recursion
        if (n == 3 or n == 1):
            return True
        if (n == 0):
            return False
        return self.isPowerOfThree(n / 3)
        """
