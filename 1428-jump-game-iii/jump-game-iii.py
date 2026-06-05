class Solution(object):
    def canReach(self, arr, start):
        memo={}
        def dfs(ind):
            if(ind<0 or ind>=len(arr)):
                return False
            if(arr[ind]==0):
                return True
            if(ind in memo):
                return memo[ind]
            memo[ind]=False
            res = dfs(ind+arr[ind]) or dfs(ind-arr[ind])
            memo[ind]=res
            return res
        return dfs(start)