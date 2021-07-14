class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == p or p == '*':
            return True
        if len(p) == 0:
            return False

        if p[0] == '*':
            matchList = p.split('*')
            for strs in matchList:
                reMatchList = strs.split('?')
                for chars in reMatchList:
                    if not chars in s:
                        return False
            # Skip '*'s in a row
            j = 1
            while j < len(p):
                if p[j] != '*':
                    break
                j += 1
            for i in range(len(s) + 1):
                if self.isMatch(s[i:], p[j:]) == True:
                    return True
        elif p[0] == '?':
            if len(s) > 0:
                if self.isMatch(s[1:], p[1:]) == True:
                    return True
        else:
            if len(s) > 0:
                if not p[len(p) - 1] in '*?' and s[len(s) - 1] != p[len(p) - 1]:
                    return False
                if s[0] == p[0]:
                    if self.isMatch(s[1:], p[1:]) == True:
                        return True
        return False
        
