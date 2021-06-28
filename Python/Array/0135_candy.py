class Solution(object):
    def candy(self, ratings: list) -> int:
        # Base Case
        if len(ratings) == 1:
            return 1

        allocate = [1]
        # Ascending order
        for i in range(1, len(ratings)):
            if ratings[i - 1] < ratings[i]:
                allocate.append(allocate[i - 1] + 1)
            else:
                allocate.append(1)
        # Descending order
        for j in range(len(ratings) - 2, -1, -1):
            if ratings[j] > ratings[j + 1] and allocate[j] <= allocate[j + 1]:
                allocate[j] = allocate[j + 1] + 1

        # Count number of candies
        count = 0
        for k in range(len(allocate)):
            count += allocate[k]

        return count
