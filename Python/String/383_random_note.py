class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if (len(ransomNote) > len(magazine)):
            return False
        elif (ransomNote == ''):
            return True
        
        ransomDict = {}
        
        # Convert magazine into a dictionary
        for char in magazine:
            ransomDict[char] = ransomDict.get(char, 0) + 1
        
        for char in ransomNote:
            # If char of ransomNote in magazine
            if (ransomDict.get(char, 0) != 0): 
                ransomDict[char] -= 1
            # If char of ransomNote not in magazine
            else:
                return False
        
        return True
        
        '''
        # Using While Loop
        
        if (len(ransomNote) > len(magazine)):
            return False
        elif (ransomNote == ''):
            return True
        
        # Convert string into an array
        ransomArray = list(ransomNote)
        
        i = 0
        while (i < len(magazine) and len(ransomArray) > 0):
            # Element in magazine found in ransomArray
            if (magazine[i] in ransomArray):
                ransomArray.remove(magazine[i])
            i += 1
        
        # All characters in ransomNote are in magazine
        if (len(ransomArray) == 0):
            return True
        return False
        '''
