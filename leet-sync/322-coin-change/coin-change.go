func coinChange(coins []int, amount int) int {
   if amount==0{
    return 0
   }
   dp:=make([]int,amount+1)
   dp[0]=0
   for i:=1;i<len(dp);i++{
    mini:=amount+1
    var curr int
    for _,val :=range coins{
        if i-val<0{
            continue
        }
        curr=dp[i-val]+1 
        if curr<mini{
            mini=curr
        }
    }
    dp[i]=mini

   }
   if dp[amount]!=amount+1{
    return dp[amount]
   }else{
    return -1
   }
   }
