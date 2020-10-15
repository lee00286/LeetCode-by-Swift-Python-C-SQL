class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negative = 1
        # Return value is negative
        if ((dividend < 0) ^ (divisor < 0)):
            negative = -1
        
        # Make dividend and divisor positive
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        # Don't need to calculate
        if (divisor == 1):
            # Overflow
            if (negative * dividend > 2**31 - 1):
                return 2**31 - 1
            return negative * dividend
        
        quotient = 0
        # Subtract dividend by divisor
        while (dividend >= divisor):
            dividend -= divisor
            quotient += 1
        
        # Overflow
        if (negative * quotient > 2**31 - 1):
            return 2**31 - 1
        return negative * quotient
