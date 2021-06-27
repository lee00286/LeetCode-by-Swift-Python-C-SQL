class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = []
        # Merge arrays nums1 and nums2
        if len(nums1) == 0 or len(nums2) == 0:
            nums3 = nums1 + nums2
        elif nums1[len(nums1) - 1] <= nums2[0]:
            nums3 = nums1 + nums2
        elif nums2[len(nums2) - 1] <= nums1[0]:
            nums3 = nums2 + nums1
        else:
            i = 0
            j = 0
            while i < len(nums1) and j < len(nums2):
                if nums1[i] <= nums2[j]:
                    nums3.append(nums1[i])
                    i += 1
                else:
                    nums3.append(nums2[j])
                    j += 1
            if i == len(nums1):
                nums3.extend(nums2[j:])
            elif j == len(nums2):
                nums3.extend(nums1[i:])

        # Even
        if len(nums3) % 2 == 0:
            return (nums3[len(nums3) // 2 - 1] + nums3[len(nums3) // 2]) / 2
        # Odd
        else:
            return nums3[len(nums3) // 2]
