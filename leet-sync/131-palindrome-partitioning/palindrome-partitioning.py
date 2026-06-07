class Solution:
    def partition(self, s: str) -> List[List[str]]:
        sol=[]
        track=[]
        def isPali(s):
            l=0
            r=len(s)-1
            while(l<r):
                if(s[r]!=s[l]):
                    return False
                l+=1
                r-=1
            return True
        def dfs(i):
            if(i==len(s)):
                sol.append(track[:])
                return 
            for j in range(i,len(s)):
                if(isPali(s[i:j+1])):
                    track.append(s[i:j+1])
                    dfs(j+1)
                    track.pop()


        dfs(0)
        return sol