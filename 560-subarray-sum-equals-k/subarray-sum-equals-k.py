class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        
        # hashmap to store prefix sum frequencies
        prefix_count = {0: 1}
        
        for num in nums:
            prefix_sum += num
            
            # check if there exists a prefix sum
            # such that current_sum - old_sum = k
            if prefix_sum - k in prefix_count:
                count += prefix_count[prefix_sum - k]
            
            # store current prefix sum
            prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1
        
        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna