class Solution {
    func countNegatives(_ grid: [[Int]]) -> Int {
        // Use the Idea of Binary Sort
        // Function to find the first occurence of negative value
        func findNegativeIndex(n: [Int]) -> Int {
            if (n[0] < 0) {
                return 0
            }
            
            var left = 0
            var right = n.count / 2
            
            while (right < n.count) {
                // Negative value is in left side
                if (n[right - 1] < 0) {
                    right -= (right - left) / 2
                }
                // Negative value is n[right]
                else if (n[right] < 0) {
                    return right
                }
                // Negative value is in right side
                else {
                    left = right
                    right += (n.count - right) / 2
                }
            }
            
            return right
        }
        
        var count = 0
        for i in (0..<grid.count) {
            // If there's negative value in grid[i]
            if (grid[i].min()! < 0) {
                count += grid[i].count - findNegativeIndex(n: grid[i])
            }
        }
        return count
    }
}
