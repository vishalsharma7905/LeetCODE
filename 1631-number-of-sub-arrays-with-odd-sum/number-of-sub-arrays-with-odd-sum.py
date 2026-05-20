class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        
        odd = 0
        even = 1   # empty prefix sum
        prefix = 0
        ans = 0
        
        for num in arr:
            prefix += num
            
            # if prefix sum is odd
            if prefix % 2 == 1:
                ans += even
                odd += 1
            else:
                ans += odd
                even += 1
        
        return ans % MOD
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna