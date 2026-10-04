# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        newNode=None
        newHead = None 
        curr = head.next
        currSum = 0 
        while curr != None:
            if curr.val!=0:
                currSum += curr.val
                curr = curr.next
            else:
                if newHead == None:
                    newHead=ListNode(currSum,None)
                    newNode = newHead
                    currSum = 0 
                    curr = curr.next
                else:
                    tempNode = ListNode(currSum,None)
                    newNode.next = tempNode
                    newNode = tempNode
                    currSum = 0 
                    curr = curr.next 
        return newHead