# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        if  not head or not head.next:
            return None
        temp=head
        n=0
        while temp:
            temp=temp.next
            n+=1
        temp=head
        prev=temp
        if n % 2 == 0:
            mid=n//2+1
        else:
            mid=(n+1)/2
        for i in range(mid-1):
            prev=temp
            temp=temp.next
        prev.next=temp.next
        return head