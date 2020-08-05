class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # One word in strs
        if (len(strs) == 1):
            return strs[0]
        if ("" in strs):
            return ""
    
        i = 0
        prefix = ""
        while (i < len(strs) - 1):
            # If first letters are different
            if (strs[i][0] != strs[i + 1][0]):
                return ""
            # If prefix doesn't fit
            if (prefix != "" and prefix[0] != strs[i][0]):
                return ""
            
            if (len(strs[i]) == 1 and len(strs[i + 1]) == 1):
                prefix = strs[i][0]
            else:
                j = 1
                if (prefix == ""):
                    minimum = min(len(strs[i]), len(strs[i + 1]))
                else:
                    minimum = min(len(prefix), len(strs[i]), len(strs[i + 1]))

                # Minimum prefix of strs[i][:j] and strs[i + 1][:j]
                while (j < minimum):
                    if (strs[i][:j] != strs[i + 1][:j]):
                        break
                    j += 1
                
                prefix = strs[i][:j - 1]
            
            i += 1
        
        return prefix
