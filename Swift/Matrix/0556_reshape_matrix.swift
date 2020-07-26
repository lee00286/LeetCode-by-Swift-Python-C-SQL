class Solution {
    func matrixReshape(_ nums: [[Int]], _ r: Int, _ c: Int) -> [[Int]] {
        let row = nums.count
        let col = nums[0].count
        // If reshape option is not possible
        if (row * col < r * c) {
            return nums
        }
        
        var cellList = [Int]()
        
        // Append all elements in cellList
        for i in (0..<row) {
            for j in (0..<col) {
                cellList.append(nums[i][j])
            }
        }
        
        var start = 0
        var end = c
        var returnList = [[Int]]()
        
        while (end <= cellList.count) {
            returnList.append(Array(cellList[start..<end]))
            start = end
            end += c
        }
        
        return returnList
    }
}
