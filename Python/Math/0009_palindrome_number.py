class Solution(object):
    # Solution without converting the integer to a string
    def isPalindrome(self, x):
        """
        
        :type x: int
        :rtype: bool
        """
        
        if (x < 0):
            return False
        
        if (x < 10):
            return True
        
        if (x < 100):
            if (x % 11 == 0):
                return True
            else:
                return False
        
        # pal is reverse of x
        pal = x % 10
        num = x // 10
        
        # Update pal
        while (num != 0):
            pal = pal * 10
            pal += num % 10
            num = num // 10
        
        return x == pal
