class Solution(object):
    def topKFrequent(self, nums, k):
        count={}
        for i in nums:
            if i in count:
                count[i]=count[i]+1
            else:
                count[i]=1
        heap = []
        for x,v in count.items():
            heapq.heappush(heap,(v,x))
            if len(heap)>k:
                heapq.heappop(heap)
        ans = [] 
        while heap:
            curr=heapq.heappop(heap)
            ans.append(curr[1])
        return ans
        