import java.lang.Math;
class Solution {
    public int mySqrt(int x) {
        if(x==0) return 0;
        if (x==1) return 1;
        float half=x/2;
        int halfx=(int) half;
        int lastx=1;
        for(int i=0;i<=halfx;i++){
            if(Math.pow(i, 2)<=x) lastx=i;
            else break;
        }
        return lastx;
    }
}