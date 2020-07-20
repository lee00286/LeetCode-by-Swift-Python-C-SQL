class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Empty String
        if (needle == ''):
            return 0
        # needle is not part of haystack
        if (needle not in haystack):
            return -1
        
        for i in range(len(haystack)):
            if (haystack[i:i + len(needle)] == needle):
                return i
