class Solution {
    func isPerfectSquare(_ num: Int) -> Bool {
        var left = 0
        var right = num
        
        while (left <= right) {
            var mid: Int = left + (right - left) / 2
            if (Int(pow(Double(mid), 2)) == num) {
                return true
            }
            else if (Int(pow(Double(mid), 2)) > num) {
                right = mid - 1
            }
            else {
                left = mid + 1
            }
        }
        return false
    }
}
