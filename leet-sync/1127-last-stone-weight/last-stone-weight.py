class Solution(object):
    def lastStoneWeight(self, stones):
        heap = [ -s for s in stones]
        heapq.heapify(heap)
        while len(heap)>1:
            s1=heapq.heappop(heap)
            s2 = heapq.heappop(heap)
            if s1!=s2:
                heapq.heappush(heap,-abs(s1-s2))

        return abs(heap[0]) if heap else 0

