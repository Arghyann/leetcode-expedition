class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        count=0
        for i in fruits:
            isPlaced=False
            for j in baskets:
                if j>=i:
                    isPlaced=True
                    print("isPlaced changed for:",)
                    baskets.remove(j)

                    break
            if not isPlaced:

                count+=1
        return count


        