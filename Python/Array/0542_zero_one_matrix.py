class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        rowNum = len(matrix)
        colNum = len(matrix[0])
        
        # Top and Left
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                # Ignore the cell with 0
                if (cell == 1):
                    # Search for 0 at the top
                    if (i != 0):
                        top = matrix[i - 1][j]
                    else:
                        top = float('inf')
                    # Search for 0 on the left
                    if (j != 0):
                        left = matrix[i][j - 1]
                    else:
                        left = float('inf')
                    
                    # Find the minimum distance
                    matrix[i][j] = min(top, left) + 1
        
        # Bottom and Right
        for i in reversed(range(rowNum)):
            for j in reversed(range(colNum)):
                cell = matrix[i][j]
                # Ignore the cell with 0
                if (cell != 0):
                    # Search for 0 at the bottom
                    if (i < rowNum - 1):
                        bottom = matrix[i + 1][j]
                    else:
                        bottom = float('inf')
                    # Search for 0 on the right
                    if (j < colNum - 1):
                        right = matrix[i][j + 1]
                    else:
                        right = float('inf')
                    
                    # Find the minimum distance
                    matrix[i][j] = min(cell, bottom + 1, right + 1)
        
        return matrix
                        
