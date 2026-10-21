import math
class Solution(object):
    def kClosest(self, points, k):
        heap = []
        for i in points:
            dist = i[0]**2+i[1]**2
            heapq.heappush(heap,(-dist,i))
            if len(heap)>k:
                heapq.heappop(heap)
        ans = []
        while heap:
            ans.append(heapq.heappop(heap)[1])
        return ans