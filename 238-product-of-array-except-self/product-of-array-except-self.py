class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [1] * n
        
        # Step 1: Prefix
        prefix = 1
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]
        
        # Step 2: Suffix
        suffix = 1
        for i in range(n-1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]
        
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna