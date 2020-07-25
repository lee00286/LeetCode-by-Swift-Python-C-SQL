class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        # Save the previous number
        prev = -1
        
        # Top to bottom, bottom to top
        if (m <= n):
            # Top to the bottom
            for col in range(n):
                prev = matrix[0][col]
                i = 1
                j = col + 1
                while (i < m and j < n):
                    # Not Toeplitz
                    if (prev != matrix[i][j]):
                        return False
                    i += 1
                    j += 1
                prev = -1

            # Bottom to the top
            for col in reversed(range(n)):
                prev = matrix[m - 1][col]
                i = m - 2
                j = col - 1
                while (i >= 0 and j >= 0):
                    # Not Toeplitz
                    if (prev != matrix[i][j]):
                        return False
                    i -= 1
                    j -= 1
                prev = -1
        # If m > n; Left to right, right to left
        else:
            # Left to the right
            for row in range(m):
                prev = matrix[row][0]
                i = row + 1
                j = 1
                while (i < m and j < n):
                    # Not Toeplitz
                    if (prev != matrix[i][j]):
                        return False
                    i += 1
                    j += 1
                prev = -1

            # Right to the left
            for row in reversed(range(m)):
                prev = matrix[row][n - 1]
                i = row - 1
                j = n - 2
                while (i >= 0 and j >= 0):
                    # Not Toeplitz
                    if (prev != matrix[i][j]):
                        return False
                    i -= 1
                    j -= 1
                prev = -1
        
        return True
