class Solution {
    public boolean asteroidsDestroyed(int mass, int[] asteroids) {
        Arrays.sort(asteroids);
        long currmass=mass;
        for(int i : asteroids){
            if(i>currmass){
                return false;
            }
            currmass=currmass+i;
        }
        return true;
    }
}