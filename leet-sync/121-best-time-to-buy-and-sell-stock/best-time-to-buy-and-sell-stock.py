class Solution(object):
    def maxProfit(self, prices):
        mini=[-1]*(len(prices))
        sell=[-1]*len(prices)
        mini[0]=prices[0]
        sell[0]=float('-inf')
        maxi=0
        for i in range(1,len(prices)):
            if(prices[i]<mini[i-1]):
                mini[i]=prices[i]
            else:
                mini[i]=mini[i-1]
            sell[i]=prices[i]-mini[i-1]
            if sell[i]>sell[maxi]:
                maxi=i
        print(sell)
        print(mini)
        if sell[maxi]>0:
            return sell[maxi]
        return 0
        