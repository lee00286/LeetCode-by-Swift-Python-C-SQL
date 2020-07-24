class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        // Dictionary [target - nums[i]:index]
        var answer: [Int : Int] = [:]

        for (i, num) in nums.enumerated() {
            // If nums[i] is in answer
            if let index = answer[target - num] {
                return [i, index]
            }

            // If num[i] is not in answer
            answer[num] = i
        }

        return []
    }
}
