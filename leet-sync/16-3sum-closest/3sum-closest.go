import (
    "sort"
    "math"
)
func threeSumClosest(nums []int, target int) int {
    sort.Ints(nums)
    closest:=nums[0]+nums[1]+nums[2]
    for i,val:=range(nums){
        left:=i+1
        right:=len(nums)-1
        for right>left{
            curr:=val+nums[left]+nums[right]
            if curr==target{
                return curr
            }
            if math.Abs(float64(target-curr))<math.Abs(float64(closest-target)){
               closest=curr 

            }
            if curr<target{
                left+=1
            }else{
               right-=1 
            }
        }
    }
    return closest
}