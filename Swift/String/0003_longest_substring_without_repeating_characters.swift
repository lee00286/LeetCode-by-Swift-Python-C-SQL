class Solution {
    func countAndSay(_ n: Int) -> String {
        // Base Case: 1
        // 2 = "11", 3 = "21", 4 = "1211", 5 = "111221"
        
        func countCon(num: String) -> String {
            var cons = ""
            var latest = ""
            var count = 0
            
            // Count number of consecutives
            for char in num {
                // First consecutive
                if (latest == "") {
                    latest = char
                    count += 1
                }
                else {
                    // If consecutive
                    if (latest == char) {
                        count += 1
                    }
                    // If not consecutive
                    else {
                        cons += (count: String) + latest
                        latest = char
                        count = 1
                    }
                }
            }
            
            cons += (count: String) + latest
            
            return cons
        }
                    
        // None Case
        if (!n || n <= 0) {
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
