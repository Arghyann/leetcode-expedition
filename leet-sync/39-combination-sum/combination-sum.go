func combinationSum(candidates []int, target int) [][]int {
    var ans [][]int
    var curr []int
    var backtrack func(i int, remaining int) 
    backtrack = func(i int , remaining int){
        if remaining==0{
            ans=append(ans,append([]int{},curr...))
            return
        }
        if i == len(candidates) || remaining<0{
            return
        }
        curr=append(curr,candidates[i])
        backtrack(i,remaining-candidates[i])
        curr=curr[:len(curr)-1]
        backtrack(i+1,remaining)
        return
    }   
    backtrack(0,target)
    return ans
}