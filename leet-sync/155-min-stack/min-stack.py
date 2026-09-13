class MinStack(object):

    def __init__(self):
         self.nums =[] 
         self.mini=[]     

    def push(self, value):
       self.nums.append(value)
       if len(self.mini) == 0:
        self.mini.append(value)
       elif value<self.mini[-1]:
        self.mini.append(value)
       else:
        self.mini.append(self.mini[-1]) 

    def pop(self):
       self.nums.pop()
       self.mini.pop()

    def top(self):
       return self.nums[-1] 

    def getMin(self):
        return self.mini[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()