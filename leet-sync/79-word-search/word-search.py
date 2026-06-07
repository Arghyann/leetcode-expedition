class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited=set()
        def dfs(m,n,k):
            if(k==len(word)):
                return True
            if(m<0 or m>=len(board) or n<0 or n>=len(board[0]) or (m,n) in visited or board[m][n]!=word[k]):
                return False
            visited.add((m,n))
            res=dfs(m+1,n,k+1) or dfs(m-1,n,k+1) or dfs(m,n+1,k+1) or dfs(m,n-1,k+1)
            visited.remove((m,n))
            return res
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0):
                    return True
        return False