class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Newton's Law
        
        r = num
        
        # if num != 1
        while (r * r > num):
            r = (r + num / r) // 2
        
        return r * r == num
    
        '''
        # Binary Search
        
        left = 0
        right = num
        
        while (left <= right):
            mid = left + (right - left) // 2
            if (mid ** 2 == num):
                return True
            elif (mid ** 2 > num):
                right = mid - 1
            else:
                left = mid + 1
        return False
        '''
    
        '''
        # Linear Search
        
        # 1 is a perfect square
        if (num == 1):
            return True
        # 2 and 3 are not perfect square
        if (num < 4):
            return False
        
        # Start from the beginning
        if (num < (2 ** 31 - 1) // 2):
            for i in range ((2 ** 31 - 1) // 2):
                if (num < i ** 2):
                    return num == (i - 1) ** 2
        # Start from the end
        else:
            for j in range (2 ** 31 - 1, (2 ** 31 - 1) // 2, -1):
                if (num > j ** 2):
                    return num == (j + 1) ** 2
        '''
            
