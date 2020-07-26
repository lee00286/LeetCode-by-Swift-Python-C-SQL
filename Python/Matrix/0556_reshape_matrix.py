class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(nums)
        col = len(nums[0])
        # If reshape option is not possible
        if (row * col < r * c):
            return nums
        
        cellList = []
        
        # Append all elements in cellList
        for i in range (row):
            for j in range(col):
                cellList.append(nums[i][j])
        
        start = 0
        end = c
        returnList = []
        
        while (end <= len(cellList)):
            returnList.append(cellList[start:end])
            start = end
            end += c
        
        return returnList
        
