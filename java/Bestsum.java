import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Bestsum{
    static Map<Integer, int[]> map = new HashMap<>();
    static int[] bestsum(int target, int[] arr){
        if(target<0) return null;
        if(target==0) return new int[]{};
        if(map.containsKey(target)) return map.get(target);
        int[] shortestcombination=null;
        for (int elem : arr) {  
            int remainder=target-elem;
            int[] computedhere = bestsum(remainder,arr); 
            if(computedhere!=null){
                
                if(shortestcombination==null || shortestcombination.length>computedhere.length+1){

                    int[] temp=Arrays.copyOf(computedhere,computedhere.length+1);
                    temp[computedhere.length]=elem;
                    shortestcombination = temp;
                }

            }

            
        }
        map.putIfAbsent(target, shortestcombination);
        return shortestcombination;

    }
    public static void main(String[] args) {


        System.out.println(Arrays.toString(
            bestsum(7, new int[]{5, 3, 4, 7})
        ));

        map.clear();
        System.out.println(Arrays.toString(
            bestsum(8, new int[]{2, 3, 5})
        ));

        map.clear();
        System.out.println(Arrays.toString(
            bestsum(100, new int[]{1, 2, 5, 25})
        ));

        map.clear();
        System.out.println(Arrays.toString(
            bestsum(300, new int[]{7, 14})
        ));
}
}