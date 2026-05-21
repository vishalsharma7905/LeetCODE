from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        dq = deque()   # stores indices
        ans = []
        
        for i in range(len(nums)):
            
            # Remove indices out of current window
            while dq and dq[0] <= i - k:
                dq.popleft()
            
            # Remove smaller elements from back
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            # Add current index
            dq.append(i)
            
            # Store answer when first window is complete
            if i >= k - 1:
                ans.append(nums[dq[0]])
        
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna