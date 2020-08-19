class Solution {
    func countAndSay(_ n: Int) -> String {
        // Base Case: 1
        // 2 = "11", 3 = "21", 4 = "1211", 5 = "111221"
        
        func countCon(num: String) -> String {
            var cons = ""
            var latest = String()
            var count = 0
            
            // Count number of consecutives
            for char in num {
                // First consecutive
                if (latest.isEmpty) {
                    latest = String(char)
                    count += 1
                }
                else {
                    // If consecutive
                    if (latest == String(char)) {
                        count += 1
                    }
                    // If not consecutive
                    else {
                        cons += String(count) + latest
                        latest = String(char)
                        count = 1
                    }
                }
            }
            
            cons += String(count) + latest
            
            return cons
        }
                    
        // None Case
        if (n <= 0) {
            return ""
        }
        // Base Case
        if (n == 1) {
            return "1"
        }
        // Recursive Case
        else {
            // Count consecutives
            return countCon(num: self.countAndSay(n - 1))
        }
    }
}
