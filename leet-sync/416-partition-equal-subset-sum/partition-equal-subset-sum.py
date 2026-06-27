class Solution(object):
    def canPartition(self, nums):
        map={}
        if(sum(nums)%2!=0):
            return False
        def dfs(req,i):
            string=str(req)+','+str(i)
            if(string in map):
                return map[string]
            if(req==0):
                return True
            if(req<0):
                return False
            if(i==len(nums)):
                return False
            ans=dfs(req-nums[i],i+1) or dfs(req,i+1)
            map[string]=ans
            return ans
        return dfs(sum(nums)//2,0)