class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # Minimum length requirement
        wordLen = len(words[0])
        minLen = len(words) * wordLen
        if (len(s) < minLen):
            return []
        
        # ====== 2) Check substring from s using hash table
        indexArr = []
        wordCount = collections.Counter(words)
        
        for i in range(len(s) - minLen + 1):
            remaining = wordCount.copy()
            wordsUsed = 0
            # Check if subStr is in words
            for j in range(i, i + minLen, wordLen):
                subStr = s[j:j + wordLen]
                if (remaining[subStr] > 0):
                    remaining[subStr] -= 1
                    wordsUsed += 1
                else:
                    break
            if (wordsUsed == len(words)):
                indexArr.append(i)
        return indexArr
    
        """
        # ====== 1) Checking all possible concatenations of words
        # ====== Time Limit Exceeded
        maxCount = -1
        for word in words:
            count = s.count(word)
            if (count == 0):
                return []
            if (count > maxCount):
                maxCount = count
        # Check all possible concatenations of words
        wordArr = []
        count = 0
        for word in itertools.permutations(words, len(words)):
            index = 0
            while (index < len(s)):
                index = s.find(''.join(word), index)
                if (index < 0):
                    break
                # If concatenation of words is found in s
                if (index not in wordArr):
                    wordArr.append(index)
                index += 1
            if (maxCount == 1 and len(wordArr) > 0):
                return wordArr
        return wordArr
        """