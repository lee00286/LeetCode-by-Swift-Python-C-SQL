class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # Two max
        a = max(nums)
        nums.remove(a)
        b = max(nums)
        nums.remove(b)
        # Two min
        c = min(nums)
        nums.remove(c)
        d = min(nums)

        # Product difference
        return (a * b) - (c * d)
