class Solution {
    func bitwiseComplement(_ N: Int) -> Int {
        var compl = 2
        
        // Nearest multiple of 2
        while (compl <= N) {
            compl = compl * 2
        }
        
        return compl - N - 1
    }
}
