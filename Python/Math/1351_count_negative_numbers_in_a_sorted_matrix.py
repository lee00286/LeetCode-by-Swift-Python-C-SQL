class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
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
