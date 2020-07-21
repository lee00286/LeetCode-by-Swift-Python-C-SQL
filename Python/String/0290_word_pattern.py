class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        
        # list of words in str
        split = str.split(' ')
        # dict e.g. {dog: a, cat: b}
        what = {}
        
        # if the number of element in array is different from pattern
        if (len(pattern) != len(split)):
            return False
        
        for i in range (len(pattern)):
            # if str not saved in what
            if (split[i] not in what):
                # if it is really a new pattern
                if (what == {}) or (pattern[i] not in pattern[:i]):
                    what[split[i]] = pattern[i]
                else:
                    return False
            elif (what[split[i]] != pattern[i]):
                return False
            
        return True
