# Dictionary Approach
class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
        # Initialize
        num = 0
        prev = 0
        
        for char in s:
            curr = romanDict[char]
            if (curr > prev):
                num = num + curr - 2 * prev
            else:
                num += curr
            prev = curr
        
        return num
