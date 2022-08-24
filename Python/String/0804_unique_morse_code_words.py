class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morseCode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        # ======== Generator Expression + Join
        return len({''.join(morseCode[ord(char) - ord('a')] for char in word) for word in words})
        
        """
        # ======== Nested For Loop + Ord
        morseDict = {}        
        for word in words:
            morseStr = ""
            for char in word:
                morseStr += morseCode[ord(char) - 96 - 1]
            morseDict[morseStr] = True
        return len(morseDict.keys())
        """