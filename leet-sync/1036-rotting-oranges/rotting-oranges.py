class Solution(object):
    def orangesRotting(self, grid):
        t=0
        new_rotten_oranges=-1
        while(new_rotten_oranges!=0):
                new_rotten_oranges=0
                for i in range(len(grid)):
                    for j in range(len(grid[0])):
                        if(grid[i][j]==2):
                            for x in range(-1,2):
                                for y in range(-1,2):
                                    if abs(x)== abs(y):
                                        continue
                                    if(i+x<len(grid) and j+y<len(grid[0]) and i+x>=0 and j+y>=0):
                                        if(grid[i+x][j+y]==1):
                                            grid[i+x][j+y]=3
                                            new_rotten_oranges+=1
                for i in range(len(grid)):
                        for j in range(len(grid[0])):
                            if(grid[i][j]==3):
                                grid[i][j]=2
                if new_rotten_oranges > 0:
                    t += 1                     
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==1):
                    return -1
        print(grid)      
        return t