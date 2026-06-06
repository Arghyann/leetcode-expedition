class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sol=[]
        curr=[]
        def dfs(i,ind):
            if(i==0):
                sol.append(curr[:])
                return
            if(i<0):
                return
            for c in range(len(candidates)):
                if(c<ind):
                    continue
                curr.append(candidates[c])
                dfs(i-candidates[c],c)
                curr.pop()
        dfs(target,0)
        return sol