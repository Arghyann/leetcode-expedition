/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int left=1;
        int right=n;
        int BadVersion=-1;
        while(left<=right){
            int mid = left + (right - left) / 2;
            if(isBadVersion(mid)){
                right=mid-1;
                BadVersion=mid;
            }
            else{
                left=mid+1;
            }
        }
        return BadVersion;
    }
}