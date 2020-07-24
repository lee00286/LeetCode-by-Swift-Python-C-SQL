class Solution {
    func checkRecord(_ s: String) -> Bool {        
        // Count number of 'A's in s
        let absent = s.filter { $0 == "A" }.count
        // If more than two continuous 'L'
        let late = s.contains("LLL")
        
        return (absent <= 1) && !late
    }
}
