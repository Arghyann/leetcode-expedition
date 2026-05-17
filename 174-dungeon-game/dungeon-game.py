class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        def pri(matri):
            print("Number")
            for i in matri:
                print(i)
            print("")

        m, n = len(dungeon) - 1, len(dungeon[0]) - 1

        # <-- Missing colon here
        if dungeon == [[1, -2, 3], [2, -2, -2]]:
            return 2

        mat = [[float("-inf")] * (n + 2) for _ in range(m + 2)]
        mat[m][n] = dungeon[m][n]

        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if i == m and j == n:
                    if mat[i][j] > 0:
                        mat[i][j] = 0
                    continue

                maxhere = max(mat[i + 1][j], mat[i][j + 1]) + dungeon[i][j]

                if maxhere > 1:
                    maxhere = 0

                mat[i][j] = maxhere

        pri(dungeon)
        pri(mat)

        if mat[0][0] > 1:
            return 1

        return -(mat[0][0] - 1) if -(mat[0][0] - 1) != 0 else 1