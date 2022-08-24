class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        halfLen = len(arr) / 2
        
        # arrHash = collections.Counter(arr)
        # occurrence = list(arrHash.values())
        occurrence = list(collections.Counter(arr).values())
        occurrence.sort()
        
        minSet = 0
        num = 0
        while (len(occurrence) > 0):
            if (num >= halfLen):
                return minSet
            num += occurrence[-1]
            occurrence.pop(-1)
            minSet += 1
        return minSet