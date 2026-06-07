class Solution {
    public int minElement(int[] nums) {
        int min=Integer.MAX_VALUE;
        for(int i: nums){
            int sum=0;
            while(i>0){
                sum=sum+i%10;
                i=i/10;
            }
            if(sum<min){
                min=sum;
            }
        }
        return min;
    }
}