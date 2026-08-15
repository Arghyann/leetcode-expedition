class Solution(object):
    def findMaxAverage(self, nums, k):
        winner=float('-inf')
        curr=0
        if(len(nums)==k):
            return sum(nums)/float(k)
        for i in range(len(nums)-k+1):
            if i == 0:
                winner=sum(nums[:k])/float(k)
                curr=winner
            else:
                curr=(-1*nums[i-1]/float(k))+(nums[i+k-1]/float(k))+curr
                if(curr>winner):
                    winner=curr
        return winner
