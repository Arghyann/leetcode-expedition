class Solution(object):
    def isValidSudoku(self, board):
        for i in range(9):
            x={}
            for j in range(9):
                
                if board[i][j] in x and board[i][j].isnumeric():
                    return False
                x[board[i][j]]=0
        

        for i in range(9):
            x={}
            for j in range(9):
                if board[j][i] in x and board[j][i].isnumeric():
                    return False
                x[board[j][i]]=0
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                x={}
                for k in range(3):
                    for l in range(3):
                        print(x)
                        if(board[i+k][j+l] in x and board[i+k][j+l].isnumeric()):
                            return False
                        x[board[i+k][j+l]]=0

        return True