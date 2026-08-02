class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo={}
        def dfs(l,r):
            if(l==r):
                return piles[l]
            if (l,r) in memo:
                return memo[(l,r)]
            lefttree=piles[l]-dfs(l+1,r)
            righttree=piles[r]-dfs(l,r-1)
            ans=max(lefttree,righttree)
            memo[(l,r)]=ans
            return ans
        ans=dfs(0,len(piles)-1)
        if ans > 0:
            return True 
        return False