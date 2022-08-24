class Solution:
    def firstUniqChar(self, s: str) -> int:
        # ====== 2) Dictionary
        repeatDict = {}
        for i in range(len(s)):
            if (s[i] not in repeatDict):
                repeatDict[s[i]] = i
            else:
                repeatDict[s[i]] = -1
        for i in repeatDict.values():
            if (i > -1):
                return i
        return -1
        
        """
        # ====== 1) For loop + Count
        for i in range(len(s)):
            if (s.count(s[i]) == 1):
                return i
        return -1
        """