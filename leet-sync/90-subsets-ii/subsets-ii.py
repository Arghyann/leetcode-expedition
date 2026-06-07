class Solution(object):
    def subsetsWithDup(self, nums):
        sol=[]
        curr=[]
        nums.sort()
        def backtrack(i):
            if i == len(nums):
                sol.append(curr[:])
                return
            curr.append(nums[i])
            backtrack(i+1)
            curr.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            backtrack(i+1)
        backtrack(0)
        return sol