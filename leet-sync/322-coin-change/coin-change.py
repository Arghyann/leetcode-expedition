class Solution(object):
    def coinChange(self, coins, amount):
        dp=[-1]*(amount+1)
        dp[0]=0
        for i in range(1,amount+1):
            coinval=[]
            for j in coins:
                if i-j>=0 and dp[i-j]!=-1:
                    coinval.append(dp[i-j]+1)
            if len(coinval)==0:
                 dp[i]=-1
            else:
                dp[i]=min(coinval)        
        return dp[amount]       
                    

        