class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Length 0
        if (len(nums1) == 0 or len(nums2) == 0):
            return []
        
        # Length 1
        if (len(nums1) == 1):
            if (nums1[0] in nums2):
                return nums1
        if (len(nums2) == 1):
            if (nums2[0] in nums1):
                return nums2
        if (len(nums1) == 1 or len(nums2) == 1):
            return []
        
        intersect = []
        
        # Loop nums1
        if (len(nums1) < len(nums2)):
            for num in nums1:
                if (num in nums2):
                    if (num not in intersect):
                        intersect.append(num)
                    nums2.remove(num)
        # Loop nums2
        else:
            for num in nums2:
                if (num in nums1):
                    if (num not in intersect):
                        intersect.append(num)
                    nums1.remove(num)
                    
        return intersect
