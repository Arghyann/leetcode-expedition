from collections import deque

class Solution(object):
    def isEscapePossible(self, blocked, source, target):

        blocked = set(map(tuple, blocked))
        LIMIT = len(blocked) * (len(blocked) - 1) // 2

        def bfs(start, end):
            q = deque([tuple(start)])
            visited = {tuple(start)}

            while q:
                x, y = q.popleft()

                if (x, y) == tuple(end):
                    return True

                if len(visited) > LIMIT:
                    return True

                for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    nx = x + dx
                    ny = y + dy
                    if (
                        0 <= nx < 10**6 and
                        0 <= ny < 10**6 and
                        (nx, ny) not in blocked and
                        (nx, ny) not in visited
                    ):
                        visited.add((nx, ny))
                        q.append((nx, ny))
            return False

        return bfs(source, target) and bfs(target, source)