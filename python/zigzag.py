class Solution(object):
    def innit(self,num):
        self.arrays={}
        for i in range(num):
            self.arrays[f'array{i}']=[]
          
            

            
    def convert(self, s, numRows):
        self.innit(numRows)
        i=0
        n=0
        while i<len(s):
            while n<numRows and i<len(s):
                self.arrays[f'array{n}']=s[i]
                i+=1
                n+=1
            n-=2    
            while 0<=n and i<len(s):
                self.arrays[f'array{n}']=s[i]
                i+=1
                n-=1
            n+=2
            string=''
            for i in range(n):
                for j in range(len(self.arrays[f'array{i}'])):
                    string+=self.arrays[f'array{i}'][j]
            
        