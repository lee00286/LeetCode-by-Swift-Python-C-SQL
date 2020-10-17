class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Don't need to calculate
        if (dividend == 0):
            return 0
        
        negative = 1
        # Return value is negative
        if ((dividend < 0) ^ (divisor < 0)):
            negative = -1
        
        # Make dividend and divisor positive
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient = 0
        # Subtract dividend by divisor
        while (dividend >= divisor):
            x = divisor
            i = 1
            while (dividend >= x + x):
                x += x
                i += i
            dividend -= x
            quotient += i
        
        # Overflow
        if (negative * quotient > 2**31 - 1):
            return 2**31 - 1
        return negative * quotient
