# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        heap = []
        listans = ListNode(0)
        curr = listans 
        for i in range(len(lists)):
            if lists[i] is not None:
                heapq.heappush(heap,(lists[i].val,i))
        while heap:
            temp = heapq.heappop(heap)
            smollist = lists[temp[1]]
            curr.next = ListNode(temp[0])
            curr = curr.next
            lists[temp[1]]=smollist.next
            if lists[temp[1]] is not None:
                heapq.heappush(heap,(lists[temp[1]].val,temp[1]))

        return listans.next