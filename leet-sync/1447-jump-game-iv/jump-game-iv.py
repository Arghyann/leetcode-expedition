from collections import defaultdict, deque

class Solution(object):
    def minJumps(self, arr):
        n = len(arr)
        if n <= 1:
            return 0
        positions = defaultdict(list)
        for i, value in enumerate(arr):
            positions[value].append(i)

        queue = deque([(0, 0)])   # (index, steps)
        visited = {0}

        while queue:
            i, steps = queue.popleft()

            if i == n - 1:
                return steps

            neighbors = positions[arr[i]] + [i - 1, i + 1]

            for nxt in neighbors:
                if 0 <= nxt < n and nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, steps + 1))

            positions[arr[i]]=[]

        return -1