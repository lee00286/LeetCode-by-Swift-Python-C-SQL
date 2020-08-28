class Solution:
    def longestPalindrome(self, s: str) -> str:
        def findPalin(l: int, r: int) -> str:
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1
            
            return s[l + 1:r]
    
        palindrome = ""
        
        for i in range(len(s)):
            # Find palin from left
            substring = findPalin(i, i)
            if (len(substring) > len(palindrome)):
                palindrome = substring
            
            # Find palin from right
            substring = findPalin(i, i + 1)
            if (len(substring) > len(palindrome)):
                palindrome = substring
    
        return palindrome
