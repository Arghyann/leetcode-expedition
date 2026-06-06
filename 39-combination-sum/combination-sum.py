class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp=[[] for k in range(target+1)]
        dp[0]=[[]]
        for num in candidates:
            for t in range(1,target+1):
                if(t-num==0):
                    dp[t].append([num])
                if t-num>0:
                    for x in dp[t-num]:
                        temp=x[:]
                        temp.append(num)
                        dp[t].append(temp)
        return dp[-1]