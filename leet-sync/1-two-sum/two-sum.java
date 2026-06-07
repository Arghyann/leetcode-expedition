import java.util.HashMap;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> harsh= new HashMap<>();
        for(int i=0;i<nums.length;i++){
            if(harsh.containsKey(target-nums[i])){
                int[] arr=new int[]{i,harsh.get(target-nums[i])};
                return arr;
            }
            harsh.put(nums[i],i);
        }
        return new int[]{-1,-1};
    }
}