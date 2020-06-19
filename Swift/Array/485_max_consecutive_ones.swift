class Solution {
    func findMaxConsecutiveOnes(_ nums: [Int]) -> Int {
        var count = 0
        var maxOnes = 0
        
        for num in nums {
            // Count consecutive ones
            if (num == 1) {
                count += 1
            }
            // If 0 occurs
            else {
                maxOnes = max(count, maxOnes)
                count = 0
            }
        }
        
        return max(count, maxOnes)
    }
}
