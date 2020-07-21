class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Using sum
        numsLen = len(nums)
        # numsLen * (numsLen + 1) // 2 is sum of numbers 0, ..., n
        return numsLen * (numsLen + 1) // 2 - sum(nums)
        
        """
        # Using loop
        numsLen = len(nums)
        
        for i in range (numsLen + 1):
            if (i not in nums):
                return i
        """
        
