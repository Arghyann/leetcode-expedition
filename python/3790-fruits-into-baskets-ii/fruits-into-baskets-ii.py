class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        count=0
        for i in fruits:
            isP=False
            for j in baskets:
                if j>=i:
                    isP=True
                    baskets.remove(j)
                    break
            if not isP:
                count+=1
        return count


        