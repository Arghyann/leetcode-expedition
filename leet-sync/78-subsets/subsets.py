class Solution(object):
    def subsets(self, nums):
        sol=[]
        curr=[]
        
        def backtrack(i):
            if(i==len(nums)):
                sol.append(curr[:])
                return 
            backtrack(i+1)
            curr.append(nums[i])
            backtrack(i+1)
            curr.pop()
        backtrack(0)
        return sol