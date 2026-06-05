class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        board = [["."] * n for _ in range(n)]

        ans = []

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

        def place(row):

            if row == n:

                temp = []

                for r in board:
                    temp.append("".join(r))

                ans.append(temp)

                return

            for col in range(n):

                if isValid(row, col):

                    board[row][col] = "Q"

                    place(row + 1)

                    board[row][col] = "."

        place(0)

        return ans