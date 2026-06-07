# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l1=ListNode()
        curr=l1
        heap=[]
        counter=0
        for i in range(len(lists)):
            if(lists[i] is not None):
                heapq.heappush(heap,(lists[i].val,counter,i))
                counter+=1
        while heap:
            temp=heapq.heappop(heap)
            curr.next=lists[temp[2]]
            curr=curr.next
            lists[temp[2]]=lists[temp[2]].next
            curr.next=None
            if(lists[temp[2]] is not None):
                heapq.heappush(heap,(lists[temp[2]].val,counter,temp[2]))
                counter+=1
            
            
            
        return l1.next