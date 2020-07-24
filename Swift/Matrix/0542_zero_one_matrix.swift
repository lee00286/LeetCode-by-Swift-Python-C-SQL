class Solution {
    func updateMatrix(_ matrix: [[Int]]) -> [[Int]] {
        var newMatrix = matrix
        var rowNum = matrix.count
        var colNum = matrix[0].count
        var maxNum = rowNum * colNum
        
        // Top and left
        for i in (0..<rowNum) {
            for j in (0..<matrix[i].count) {
                // Ignore the cell with 0
                if (newMatrix[i][j] == 1) {
                    // Search for 0 at the top
                    let top = (i != 0) ? newMatrix[i - 1][j] : maxNum
                    // Search for 0 on the left
                    let left = (j != 0) ? newMatrix[i][j - 1] : maxNum
                    
                    // Find the minimum distance
                    newMatrix[i][j] = min(top, left) + 1
                }
            }
        }
        
        // Bottom and Right
        for i in (0..<rowNum).reversed() {
            for j in (0..<colNum).reversed() {
                let cell = newMatrix[i][j]
                // Ignore the cell with 0
                if (cell != 0) {
                    // Search for 0 at the bottom
                    let bottom = (i < rowNum - 1) ? newMatrix[i + 1][j] : maxNum
                    // Search for 0 on the right
                    let right = (j < colNum - 1) ? newMatrix[i][j + 1] : maxNum
                    
                    // Find the minimum distance
                    newMatrix[i][j] = min(cell, bottom + 1, right + 1)
                }
            }
        }
        
        return newMatrix
    }
}
