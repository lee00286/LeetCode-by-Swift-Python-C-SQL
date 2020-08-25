class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(x):
            length = len(x)
            for i in range(int(length/2)):
                if (x[i] != x[length - i - 1]): 
                    return False
            return True
        
        # If s is palindrome
        if isPalindrome(s): 
            return s
        
        dicPalin = {}
        
        length = len(s)
        
        for i in range(len(s) - 1):
            j = 0
            while (j < length):
                if (s[length - j - 1] == s[i]):
                    if (isPalindrome(s[i:length - j])):
                        dicPalin[i] = length - j - i
                        break
                j += 1
        
        key = max(dicPalin, key=dicPalin.get)
    
        return s[key:dicPalin[key] + key]
