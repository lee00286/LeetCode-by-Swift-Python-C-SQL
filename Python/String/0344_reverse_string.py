class Solution(object):        
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        def swap(start, end, s):
            if (start >= end):
                return None
            # Swap two strings
            s[start], s[end] = s[end], s[start]

            swap(start + 1, end - 1, s)
        
        return swap(0, len(s) - 1, s)
