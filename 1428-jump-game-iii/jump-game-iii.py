class Solution(object):
    def canReach(self, arr, start):
        # Create an empty set to store visited indices
        visited = set()

        def dfs(i):
            # Out of bounds
            if i < 0 or i >= len(arr):
                return False

            # Already visited
            if i in visited:
                return False

            # Found a zero
            if arr[i] == 0:
                return True

            # Mark as visited
            visited.add(i)

            # Try both possible jumps
            return dfs(i + arr[i]) or dfs(i - arr[i])

        return dfs(start)