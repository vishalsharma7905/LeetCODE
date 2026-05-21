class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = prices[0]
        max_profit = 0
        
        for price in prices:
            
            # Update minimum buying price
            min_price = min(min_price, price)
            
            # Calculate profit
            profit = price - min_price
            
            # Update maximum profit
            max_profit = max(max_profit, profit)
        
        return max_profit

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna