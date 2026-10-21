import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        heap = []
        for i in range(k):
            heapq.heappush(heap,nums[i])
        for i in range(i+1,len(nums)):
            if nums[i]>heap[0]:
                heapq.heapreplace(heap,nums[i])
        return heap[0]