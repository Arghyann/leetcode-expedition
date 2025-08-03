class Solution(object):
    def permute(self, nums):
        sol,ans=[],[]

        def backtrack():
            if len(sol)==len(nums):
                ans.append(sol[:])
                

            for k in nums:
                if k not in sol:
                    sol.append(k)
                    backtrack()
                    sol.pop()
                
        backtrack()
        return ans