import copy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        board = [["."] * n for _ in range(n)]

        def isValid(row, col):
            for r in range(row):
                if board[r][col] == "Q":
                    return False
            r, c = row - 1, col - 1

            while r >= 0 and c >= 0:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c -= 1
            r, c = row - 1, col + 1

            while r >= 0 and c < n:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c += 1

            return True
        ans=[]
        def place(d):
            if d==n:
                temp=["".join(row) for row in board]
                ans.append(temp)
                return True
            for i in range(n):
                if(isValid(d,i)):
                    board[d][i]='Q'
                    place(d+1)
                    board[d][i]='.'
            return False
        place(0)
        return ans