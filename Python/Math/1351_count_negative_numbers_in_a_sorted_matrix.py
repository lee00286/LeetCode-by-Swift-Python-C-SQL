class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # Use the Idea of Binary Sort
        # Function to find the first occurence of negative value
        def findNegativeIndex(n: List[int]) -> int:
            if (n[0] < 0):
                return 0
            
            left = 0
            right = len(n) // 2
            
            while (right < len(n)):
                # Negative value is in left side
                if (n[right - 1] < 0):
                    right -= (right - left) // 2
                # Negative value is n[right]
                elif (n[right] < 0):
                    return right
                # Negative value is in right side
                else:
                    left = right
                    right += (len(n) - right) // 2
        
        count = 0
        for i in range(len(grid)):
            # If there's negative value in grid[i]
            if (min(grid[i]) < 0):
                count += len(grid[i]) - findNegativeIndex(grid[i])
        return count
    
        '''
        # Function to check if the list contains negatives
        def isListSumEqual(n: List[int]) -> bool:
            nSum = 0
            absSum = 0
            
            for i in range(len(n)):
                nSum += n[i]
                absSum += abs(n[i])
            
            return nSum == absSum
        
        count = 0
        
        for i in range(len(grid)):
            # If the list contains negatives
            if (not isListSumEqual(grid[i])):
                for j in range(len(grid[i])):
                    # Count negatives
                    if (grid[i][j] < 0):
                        count += 1
        
        return count
        '''
