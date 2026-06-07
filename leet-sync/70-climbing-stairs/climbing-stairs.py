class Solution(object):
    def climbStairs(self, n):
       count=1
       nprev=0
       nprevprev=0
       for i in range(n):
            print(count,nprev)
            nprevprev = nprev
            nprev=count
            count=nprev+nprevprev
            
       return count