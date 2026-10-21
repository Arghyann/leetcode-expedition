import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
       rev = [-i for i in nums] 
       heapq.heapify(rev)
       num = -1
       for i in range(k):
        num=heapq.heappop(rev) 
       return -num