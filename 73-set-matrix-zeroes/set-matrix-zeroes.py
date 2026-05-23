class Solution:
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        row = set()
        col = set()

        # Find positions of 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)

        # Set rows to 0
        for i in row:
            for j in range(cols):
                matrix[i][j] = 0

        # Set columns to 0
        for j in col:
            for i in range(rows):
                matrix[i][j] = 0

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna