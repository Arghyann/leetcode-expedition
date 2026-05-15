
import java.util.ArrayList;
import java.util.List;

class BestSumTab{
    static List<Integer> bestsum(int target, int[] arr){
        List<List<Integer>> list=new ArrayList<>();
        for(int i=0;i<=target;i++){
            list.add(null);
        }
        list.set(0, new ArrayList<>());
        for(int i=0;i<list.size();i++){
            for(int x : arr){
                if(list.get(i)!=null && (i+x)<list.size()){
                    List<Integer> temp=new ArrayList<>(list.get(i));
                    temp.add(x);
                    if(list.get(i+x)==null){
                        list.set(i+x,temp);
                    }
                    if(list.get(i+x)!=null){
                        if(list.get(i+x).size()>temp.size()){
                            list.set(i+x,temp);
                        }
                    }
                    
                    
                    
                }

            }
            
        }
        if(list.get(target)!=null) return list.get(target);
        return new ArrayList<>();
    }

    static void test(int target, int[] arr) {
        System.out.println(
            "target=" + target +
            ", arr=" + java.util.Arrays.toString(arr) +
            " => " + bestsum(target, arr)
        );
}

    public static void main(String[] args) {
        test(7, new int[]{2, 3});          // expected: sums to 7
        test(7, new int[]{5, 3, 4, 7});    // expected: [7] or [3,4]/[4,3]
        test(7, new int[]{2, 4});          // expected: []
        test(8, new int[]{2, 3, 5});       // expected: sums to 8
        test(0, new int[]{1, 2, 3});       // expected: []
        test(1, new int[]{2, 3});          // expected: []
        test(300, new int[]{7, 14,2});       // expected: []
    }
}