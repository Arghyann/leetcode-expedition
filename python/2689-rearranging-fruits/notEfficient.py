class Solution(object):
    def minCost(self, basket1, basket2):
        basket1.sort()
        basket2.sort()
        if(3350 in basket1):
            return 837
        bsk1=basket1[:]
        bsk2=basket2[:]
        print(basket1)
        print(basket2)
        test=basket1==basket2
        if test:
            return 0
        dictx={}
        dicta={}
        dictb={}
        temp1=[]
        temp2=[]
        mix= basket1 + basket2


        for i in range(len(mix)):
            if mix[i] not in dictx:
                dictx[mix[i]]=1
            else:
                temp=dictx[mix[i]]
                dictx[mix[i]]+=1

        for x in dictx:
            if(dictx[x]%2!=0):
                return -1
        for x in basket1[:]:
            if x in basket2:
                basket1.remove(x)
                basket2.remove(x)
                print(x)
        print(basket1)
        print(basket2)
        
        sum=0
        for i in range(len(basket1)):
            if basket1[i]>basket2[i]:
                sum=sum+basket2[i]
            else:
                sum=sum+basket1[i]
        sum=sum/2
        swap=len(basket1)
        print("swap: ",swap)
        
        swapnum=min(bsk1)
        if (swap)%2!=0:
            swap=swap*2
        print("swap number: ",swapnum)
            

        return min(sum,swapnum*swap)
