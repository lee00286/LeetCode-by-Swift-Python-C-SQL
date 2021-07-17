class Solution:
    # ISSUE: Time Limit Exceeded
    def firstMissingPositive(self, nums: List[int]) -> int:
        if max(nums) <= 0:
            return 1
        for i in range(len(nums)):
            if nums[i] < 0 or nums[i] > len(nums):
                nums[i] = 0

        if (min(nums) > 1):
            return 1
        num = min(min(nums), 0) + 1
        while num < max(nums):
            if num in nums:
                num += 1
            else:
                return num
        return max(nums) + 1
