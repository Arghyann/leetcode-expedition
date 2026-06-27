class Solution(object):
    def minDistance(self, word1, word2):
        dp = [[0]* (len(word1)+1) for k in range(len(word2)+1)] 
        for i in range(len(word1)):
            dp[len(word2)][i]=len(word1)-i
        for j in range(len(word2)):
            dp[j][len(word1)]=len(word2)-j
        for i in range(len(word2)-1,-1,-1):
            for j in range(len(word1)-1,-1,-1):
                if(word1[j]==word2[i]):
                    dp[i][j]=dp[i+1][j+1]
                else:
                    insert=dp[i+1][j]
                    delete=dp[i][j+1]
                    replace=dp[i+1][j+1]
                    dp[i][j]=1+min(insert,delete,replace)
        return dp[0][0]