class Solution {
    func isToeplitzMatrix(_ matrix: [[Int]]) -> Bool {
        let m = matrix.count
        let n = matrix[0].count
        // Save the previous number
        var prev = -1
        
        // Top to bottom, bottom to top
        if (m <= n) {
            // Top to the bottom
            for col in 0..<n {
                prev = matrix[0][col]
                var i = 1
                var j = col + 1
                while (i < m && j < n) {
                    // Not Toeplitz
                    if (prev != matrix[i][j]) {
                        return false
                    }
                    i += 1
                    j += 1
                }
                prev = -1
            }

            // Bottom to the top
            for col in (0..<n).reversed() {
                prev = matrix[m - 1][col]
                var i = m - 2
                var j = col - 1
                while (i >= 0 && j >= 0) {
                    // Not Toeplitz
                    if (prev != matrix[i][j]) {
                        return false
                    }
                    i -= 1
                    j -= 1
                }
                prev = -1
            }
        }
        // If m > n; Left to right, right to left
        else {
            // Left to the right
            for row in 0..<m {
                prev = matrix[row][0]
                var i = row + 1
                var j = 1
                while (i < m && j < n) {
                    // Not Toeplitz
                    if (prev != matrix[i][j]) {
                        return false
                    }
                    i += 1
                    j += 1
                }
                prev = -1
            }

            // Right to the left
            for row in (0..<m).reversed() {
                prev = matrix[row][n - 1]
                var i = row - 1
                var j = n - 2
                while (i >= 0 && j >= 0) {
                    // Not Toeplitz
                    if (prev != matrix[i][j]) {
                        return false
                    }
                    i -= 1
                    j -= 1
                }
                prev = -1
            }
        }
        
        return true
    }
}
