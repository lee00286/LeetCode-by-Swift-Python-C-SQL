class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Base Cases
        if (s == ''):
            return 0
        if (len(s) == 1):
            return 1
        
        dicSub = {}
        left = 0
        largest = 0
        
        for i in range(len(s)):
            if (s[i] in dicSub):
                largest = max(largest, i - left)
                left = max(left, dicSub[s[i]] + 1)
            dicSub[s[i]] = i
            
        return max(largest, len(s) - left)
    
        '''
        # Using for loop
        
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
                largest = max(largest, count)
                count = 1
                before = i - 1
            else:
                count = i - before + 1
        
        largest = max(largest, count)
        
        return largest
        '''
