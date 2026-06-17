class Solution(object):
    def lengthOfLIS(self, nums):
        dp=[ 0 for _ in range(len(nums))]
        dp[0]=1
        for i in range(len(nums)):
            lowest=[-1,-1]
            for j in range(0,i):
                if(nums[j]<nums[i] and dp[j]>lowest[1]):
                    lowest=[j,dp[j]]
            if(lowest[0]==-1):
                dp[i]=1
            else:
                dp[i]=lowest[1]+1
        return max(dp)