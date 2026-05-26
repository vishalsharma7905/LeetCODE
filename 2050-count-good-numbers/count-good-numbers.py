class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        even_positions = (n + 1) // 2
        odd_positions = n // 2

        return (pow(5, even_positions, MOD) *
                pow(4, odd_positions, MOD)) % MOD

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna