class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        count=0
        for i in fruits:
            print("i here first",i)
            isPlaced=False
            for j in baskets:
                if j>=i:
                    print("i here again:",i)
                    isPlaced=True
                    print("isPlaced changed for:", i)

                    baskets.remove(j)
                    print(j)
                    print(baskets)
                    break
            if not isPlaced:
                print("count increased for: ",i )
                count+=1
        return count


        