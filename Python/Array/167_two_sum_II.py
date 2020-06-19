class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        
        >>> twoSum([2, 7, 11, 15], 9)
        [1, 2]
        """
        
        answer = {}
        for i in range(1, len(numbers) + 1):
            num = numbers[i - 1]
            if (num not in answer):
                answer[target - num] = i
            else:
                return [answer[num], i]
