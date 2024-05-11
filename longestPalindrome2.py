class Solution:
    def longestPalindrome(self,s):
        result=s[0]
        
        for i in range(len(s)-1):
            #for odd cases
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            if(r-l-1>len(result)): 
                result=s[l+1:r]
                

            #for even result
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                
                l-=1
                r+=1
                
            
            if(r-l-1>len(result)): 
                
                result=s[l+1:r]
                
        
        return result
             
            
solution=Solution()
print(solution.longestPalindrome("cbbd"))           
#two fucking hours to figure this out wow

