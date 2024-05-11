class node:
    def __init__(self,value,next=None):
        self.value=value
        self.next=next
class LinkedList:
    def __init__(self,head=None):
        self.head=head
    def insert(self,val):
        node1=node(val)
        if self.head is None:
            self.head=node1
            return
        else:
            currentNode=self.head
            while(currentNode.next is not None):
                currentNode=currentNode.next
            currentNode.next=node1
    
    def printLl(self):
         currentNode=self.head
         while True:
                print(currentNode.value,end="->")
                if currentNode.next is None:
                    print("none")
                    break
                currentNode=currentNode.next
l1=LinkedList()

l1.insert(9)
l1.printLl()
l1.insert(21)
l1.printLl()

