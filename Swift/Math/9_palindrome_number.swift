class Solution {
    func isPalindrome(_ x: Int) -> Bool {
        if (x < 0) {
            return false
        }
        
        if (x < 10) {
            return true
        }
        
        if (x < 100) {
            if (x % 11 == 0) {
                return true
            }
            else {
                return false
            }
        }
        
        // pal is reverse of x
        var pal = x % 10
        var num = x / 10
        
        // Update pal
        while (num != 0) {
            pal = pal * 10
            pal += num % 10
            num = num / 10
        }
        
        return x == pal
    }
}
