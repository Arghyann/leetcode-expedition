import java.util.Arrays;
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] arryl=new int[nums.length];
        int[] arryr=new int[nums.length];
        int prodl=1;
        int prodr=1;
        arryl[0]=1;
        for(int i=1;i<nums.length;i++){
            prodl=nums[i-1]*prodl;
            arryl[i]=prodl;
        }
        arryr[nums.length-1]=1;
        for(int i=nums.length-2;i>=0;i--){
            prodr=nums[i+1]*prodr;
            arryr[i]=prodr;
            
        }
        int[] result = new int[nums.length];
        for(int i = 0; i<nums.length;i++){
            result[i]=arryl[i] * arryr[i];
        }
        return result;
    }

}