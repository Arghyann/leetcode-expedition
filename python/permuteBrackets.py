class Solution:
    def diffWaysToCompute(self, expression: str):
        signs=[]
        for i in expression:
            if not i.isnumeric():
                signs.append(i)
        for i in range(len(signs)):
            newsigns=signs[:]
            del newsigns[i]
            self.diffWaysToCompute(newsigns)


solution=Solution()
exp="2-1-1"
print(solution.diffWaysToCompute(exp))