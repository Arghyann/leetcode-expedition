class Solution {
    public int numberOfSpecialChars(String word) {
        HashMap<Character, Integer> mapL = new HashMap<>();
        HashMap<Character, Integer> mapU = new HashMap<>();
        int count = 0;
        for(int i=0; i<word.length();i++){
            char ch = word.charAt(i);
            if(Character.isLowerCase(ch)){
                mapL.put(ch,i);
            }
            else{
                mapU.putIfAbsent(ch,i);
            }
        }
        for(Character c : mapU.keySet()){
            char cl = Character.toLowerCase(c);
            if(mapL.get(cl)!=null && mapL.get(cl)<mapU.get(c)){
                count=count+1;
            }
        }
        return count;
    }
}