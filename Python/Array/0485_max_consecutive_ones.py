class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = 0
        maxOnes = 0
        
        for num in nums:
            # Count consecutive ones
            if (num == 1):
                count += 1
            # If 0 occurs
            else:
                maxOnes = max(count, maxOnes)
                count = 0
        
        return max(count, maxOnes)
        
        """
        # Use index of 0
        maximum = 0
        while (0 in nums):            
            # Find the index of 0
            numIndex = nums.index(0)
            
            # Update maximum
            maximum = max(numIndex, maximum)
            
            # Update nums
            if (numIndex == len(nums)):
                return maximum
            else:
                nums = nums[numIndex + 1:]
        
        return max(len(nums), maximum)
        """
        
