class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Symbol | Value       Symbol | Value
        -------+-------      -------+-------
        I      | 1           IV     | 4
        V      | 5           IX     | 9
        X      | 10          XL     | 40
        L      | 50          XC     | 90
        C      | 100         CD     | 500
        D      | 500         CM     | 900
        M      | 1000
        """
        result = 0
        romanDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        i = 0
        while (i < len(s) - 1):
            # if (s[i:i + 2] in ["IV", "IX", "XL", "XC", "CD", "CM"]):
            if (romanDict[s[i]] < romanDict[s[i + 1]]):
                result += romanDict[s[i + 1]] - romanDict[s[i]]
                i += 1
            else:
                result += romanDict[s[i]]
            i += 1
        if (i < len(s)):
            result += romanDict[s[i]]
        return result