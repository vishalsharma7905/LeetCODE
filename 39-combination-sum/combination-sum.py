class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []

        def backtrack(i, curr, total):

            if total == target:
                ans.append(curr.copy())
                return

            if i >= len(candidates) or total > target:
                return

            # take current number
            curr.append(candidates[i])
            backtrack(i, curr, total + candidates[i])

            # undo choice
            curr.pop()

            # skip current number
            backtrack(i + 1, curr, total)

        backtrack(0, [], 0)
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna