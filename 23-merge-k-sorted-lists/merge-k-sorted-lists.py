# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l1=ListNode()
        curr=l1
        while True:
            flag=False
            for i in range(len(lists)):
                if(lists[i] is not None):
                    flag=True
                    break
            if not flag:
                break
            mint=[float('inf'),-1]
            for i in range(len(lists)):                
                if(lists[i] is not None and lists[i].val<mint[0]):
                    mint=[lists[i].val,i]
            curr.next=lists[mint[1]]
            lists[mint[1]]=lists[mint[1]].next
            curr=curr.next
            curr.next=None
            curr.val=mint[0]
            
        return l1.next