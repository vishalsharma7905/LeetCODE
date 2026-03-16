class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) > 1:
            new = []
            
            for i in range(len(nums)//2):
                if i % 2 == 0:
                    new.append(min(nums[2*i], nums[2*i+1]))
                else:
                    new.append(max(nums[2*i], nums[2*i+1]))
            
            nums = new
        
        return nums[0]