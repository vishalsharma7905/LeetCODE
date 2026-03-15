class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max1 = -1
        max2 = -1
        idx = -1
        
        for i, n in enumerate(nums):
            if n > max1:
                max2 = max1
                max1 = n
                idx = i
            elif n > max2:
                max2 = n
        
        if max1 >= 2 * max2:
            return idx
        return -1