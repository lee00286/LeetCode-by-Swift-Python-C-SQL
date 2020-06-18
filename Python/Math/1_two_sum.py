class Solution(object):
    def twoSum(self, nums, target):
        """
        >>> twoSum([2, 7, 11, 15], 9)
        [0, 1]
        >>> twoSum([3, 3, 2],6)
        [0, 1]
        """

        # Dictionary {target - nums[i]:index}
        answer = {}
        for i in range(len(nums)):
            number = nums[i]
            # If num[i] is not in answer
            if number not in answer:
                answer[target - number] = i
            # If num[i] is in answer
            else:
                return [i, answer[number]]

        return result
