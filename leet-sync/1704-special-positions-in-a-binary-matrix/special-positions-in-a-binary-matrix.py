class Solution(object):
    def numSpecial(self, mat):
        count = 0
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    row_sum = sum(mat[i])
                    col_sum = sum(mat[r][j] for r in range(m))
                    if row_sum == 1 and col_sum == 1:
                        count += 1
        return count