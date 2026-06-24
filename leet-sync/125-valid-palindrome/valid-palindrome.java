class Solution {
    public boolean isPalindrome(String s) {
        String temp=s.toLowerCase();
        temp=temp.replaceAll("[^a-z0-9]","");
        temp=temp.replace(" ","");
        System.out.println(temp);
        int left=0;
        int right = temp.length()-1;
        while(left<right){
            if(temp.charAt(left)!=temp.charAt(right)){
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}