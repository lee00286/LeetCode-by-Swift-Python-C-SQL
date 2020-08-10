class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Base Cases
        if (s == ''):
            return 0
        if (len(s) == 1):
            return 1
        
        count = 1
        largest = 1
        before = 0
        for i in range(1, len(s)):
            if (s[i] in s[before:i]):
                if (count > largest):
                    largest = count
                count = 0
                before = i - 1
            else:
                count += 1
        
        return largest
