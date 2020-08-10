class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Base Cases
        if (s == ''):
            return 0
        if (len(s) == 1):
            return 1
        
        count = 0
        largest = 0
        before = 0
        for i in range(len(s)):
            if (s[i] in s[before:i]):
                if (count > largest):
                    largest = count
                count = 0
                before = i
            else:
                count += 1
        
        return largest
