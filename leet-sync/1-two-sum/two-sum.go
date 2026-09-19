func twoSum(nums []int, target int) []int {
   m := make(map[int]int) 
   for i,val := range nums{
        valinmap,ok := m[target-val]
        if !ok{
            m[val]=i
        } else{
            return []int{valinmap,i}
        }
     
   }
   return []int{}
}