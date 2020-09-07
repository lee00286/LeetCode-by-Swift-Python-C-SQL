class Solution {
    func lengthOfLongestSubstring(_ s: String) -> Int {
        // Base Cases
        if (s == "") {
            return 0
        }
        if (s.count == 1) {
            return 1
        }
        
        //var dicSub = ["star": 0]
        var dicSub: [Character: Int] = [:]
        var left = 0
        var largest = 0
        
        for (i, char) in s.enumerated() {
            if (dicSub[char] != nil) {
                largest = max(largest, i - left)
                left = max(left, dicSub[char]! + 1)
            }
            dicSub.updateValue(i, forKey: char)
        }
            
        return max(largest, s.count - left)
    }
}
