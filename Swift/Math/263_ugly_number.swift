class Solution {
    func isUgly(_ num: Int) -> Bool {        
        if (num <= 0) {
            return false
        }
        
        var n = num
        
        while (n != 1) {
            // Divisible by 2
            if (n % 2 == 0) {
                n /= 2
            }
            // Divisible by 3
            else if (n % 3 == 0) {
                n /= 3
            }
            // Divisible by 5
            else if (n % 5 == 0) {
                n /= 5
            }
            // Prime factors include other than 2, 3, 5
            else {
                return false
            }
        }
        
        return true
    }
}
