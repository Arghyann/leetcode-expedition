class Solution(object):
    def totalWaviness(self, num1, num2):
        wvns=0
        for i in range(num1,num2+1):
            digits=[]
            j=i
            while j>0:
                digits.append(j%10)
                j=j//10
            for k in range(1,len(digits)-1):
                if(digits[k]>digits[k-1] and digits[k]>digits[k+1]):
                    wvns+=1
                elif(digits[k]<digits[k-1] and digits[k]<digits[k+1]):
                    wvns+=1
        return wvns
        