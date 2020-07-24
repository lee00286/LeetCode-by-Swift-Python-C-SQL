class Solution {
    func isPowerOfThree(_ n: Int) -> Bool {
        // Division
        if (n < 1) {
            return false;
        }
        
        var num = n        
        while (num % 3 == 0) {
            num /= 3
        }
        
        return num == 1
        
        /*
        // Recursion
        if (n < 1) {
            return false
        }
        else if (n == 1) {
            return true
        }
        else {
            // Recursion
            return n % 3 == 0 && isPowerOfThree(n / 3)
        }
        */
    }
}
