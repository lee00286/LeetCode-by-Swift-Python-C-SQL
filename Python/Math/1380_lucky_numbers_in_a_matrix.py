class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        index = 0
        minimum = 0
        flag = 0
        result = []
        
        for i in matrix:
            minimum = min(i)
            # Minimum element in its row
            index = i.index(minimum)
            # Maximum element in its column
            for j in matrix:
                if (j[index] > minimum):
                    flag = 1
                    break
            # Add to the result array
            if (flag == 0):
                result.append(minimum)
            
            index = 0
            minimum = 0
            flag = 0
        
        return result
