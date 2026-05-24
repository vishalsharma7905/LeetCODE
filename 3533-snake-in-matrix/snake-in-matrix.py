class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        row = 0
        col = 0

        for command in commands:
            if command == "UP":
                row -= 1
            elif command == "DOWN":
                row += 1
            elif command == "LEFT":
                col -= 1
            else:  # RIGHT
                col += 1

        return row * n + col

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna