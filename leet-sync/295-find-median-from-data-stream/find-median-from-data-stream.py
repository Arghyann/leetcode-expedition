class MedianFinder(object):

    def __init__(self):
       self.smallheap=[] 
       self.bigheap=[]

    
    def addNum(self, num):
        heapq.heappush(self.smallheap,-num)
        heapq.heappush(self.bigheap,-heapq.heappop(self.smallheap))
        if len(self.bigheap)>len(self.smallheap):
            heapq.heappush(self.smallheap,-heapq.heappop(self.bigheap))
    def findMedian(self):
       if len(self.smallheap)==len(self.bigheap):
        return float(-self.smallheap[0]+self.bigheap[0])/2.0
       return -self.smallheap[0] 
       


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()