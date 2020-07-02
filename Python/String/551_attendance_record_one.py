class Solution:
    def checkRecord(self, s: str) -> bool:
        if (len(s) > 1):
            if ('A' in s or 'L' in s):
                # More than two continuous 'L'
                if ('LLL' in s):
                    return False
                if ('A' in s):
                    if (s.find('A') < len(s) - 1 and 'A' in s[s.find('A') + 1:]):
                        return False
        return True
