class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        count=0
        for i in range(len(fruits)):
            
            isPlaced=False
            for j in range(len(baskets)):
                if baskets[j]>=fruits[i]:
                    
                    isPlaced=True
                   

                    baskets.pop(j)
                    print(j)
                    print(baskets)
                    break
            if not isPlaced:
                
                count+=1
        return count


        