class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket = {'(': ')', '{': '}', '[': ']'}
        copy_s = ''
        
        if (len(s) % 2 == 0):
            for i in range(len(s)):
                if s[i] in bracket and bracket[s[i]] in s[i:]:
                    copy_s += s[i]
                elif s[i] not in bracket:
                    if (copy_s != '' and bracket[copy_s[-1]] == s[i]):
                        copy_s = copy_s[:-1]
                    else:
                        return False
                else:
                    return False
            return True
        return False
        
