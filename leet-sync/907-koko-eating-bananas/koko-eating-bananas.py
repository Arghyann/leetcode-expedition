from math import ceil
class Solution(object):
    def minEatingSpeed(self, piles, h):
        def consume(speed):
            tot=0
            for i in range(len(piles)):
                turn = (piles[i] + speed - 1) // speed
                tot+=turn
            if tot>h:
                return False
            else: 
                return True
        left=1
        right=max(piles)
        while left<right:
            mid=left+(right-left)//2
            if consume(mid):
                right=mid
            else:
                left=mid+1
        return left         