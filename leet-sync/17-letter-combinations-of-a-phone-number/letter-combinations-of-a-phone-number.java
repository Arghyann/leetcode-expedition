class Solution {
    String[] arr={"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
    List<String> sol = new ArrayList<>();
    public List<String> letterCombinations(String digits) {
        backtrack(digits,0,"");
        return sol;
    }
    public void backtrack(String s,int index,String current){
        if(index==s.length()){
            sol.add(current);
            return;
        }
        String possible=arr[s.charAt(index)-'0'];
        for(int i =0;i<possible.length();i++){
            String temp=current+possible.charAt(i);
            backtrack(s,index+1,temp);
        }

    }
}