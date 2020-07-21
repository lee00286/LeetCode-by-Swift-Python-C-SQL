class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        alphabetArray = []
        
        # First, second, and third row
        for row in [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]:
            for word in words:
                # Compare word and row
                if (set(word.lower()) <= row):
                    alphabetArray.append(word)
        
        return alphabetArray
