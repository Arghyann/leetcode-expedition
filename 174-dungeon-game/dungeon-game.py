class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # Get dimensions of the dungeon
        rows, cols = len(dungeon), len(dungeon[0])
      
        # Initialize DP table with infinity values
        # Extra row and column for boundary conditions
        dp = [[float('inf')] * (cols + 1) for _ in range(rows + 1)]
      
        # Set base cases: minimum health needed just outside the princess room is 1
        dp[rows][cols - 1] = dp[rows - 1][cols] = 1
      
        # Fill DP table from bottom-right to top-left
        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                # Minimum health needed at current cell is:
                # - At least 1 (knight must survive)
                # - Minimum health from next cell minus current cell's value
                min_health_on_exit = min(dp[row + 1][col], dp[row][col + 1])
                dp[row][col] = max(1, min_health_on_exit - dungeon[row][col])
      
        # Return minimum initial health needed at starting position
        return dp[0][0]