class Solution {
    List<List<Integer>> result= new ArrayList<>();
    List<Integer> sol=new ArrayList<>();
    public List<List<Integer>> subsets(int[] nums) {
        backtrack(0,nums);
        return result;
    }
    public void backtrack(int i,int[] nums){
        if(i==nums.length){
            result.add(new ArrayList<>(sol));
            return;
        }
        
        backtrack(i + 1, nums);
        sol.add(nums[i]);
        backtrack(i + 1, nums);
        sol.remove(sol.size() - 1);
    }
}   
