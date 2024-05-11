#original brute force approach that took too much time for leetcode
class Solution(object):
    def everysubs(self, s):
        array=[]
        for i in range(1,len(s)+1):
            for j in range(len(s)-i+1):
                
                    array.append(s[j:j+i])
        return array
    def longestPalindrome(self,s):
         array=self.everysubs(s)
         result=''
         for i in range(len(array)):
              temp=array[i][::-1]
              if(array[i]==temp and len(array[i])>len(result)):
                   result=array[i]
         return result
    
         

solution=Solution()

print(solution.longestPalindrome("jfbnhnjamsfsbsslcaaivnzryrrkcqmektqjnymeifxvvskicpxxrztysetlpucxfqccmeyptxxziqhacxatxjynmbblssyaxvcmbtyrtqfwxrwsgfrinfkczktytwglbrskeogamecvihkywnljnqfmrrnqcvopcoyroncwzhdqzvwdbtjmcocwljjvipabzorajqgiabqjeyasbrjvyjtdvgupqtmydfgdczaodyokxxarfboxifcltizhhntciffijclljvdfgpsojwmupgtrbquuzjdefnmxtcaborisjcsavucmuovlksonzvmmuvujzirioxdcadeioravjoyxhrqevfwmxacimtvbmfweqpvfijyuqrjfgejrnlmhvbbmbvviilsothgvaqgqtllonrqbsltwpikfrckdhttxzmbqmbhbjjwfddnrfwtafgjtuqyatkpcavokouftqwdzfclkckwzfwlozksgkrcyimvdhfrzlqqxnfhjkwfiewwqmbfyjdjematsvusmqxzwfyukqwlfzzyzlkqvgmq"))
