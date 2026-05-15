import java.util.HashMap;
import java.util.Map;
public class Fib {
    static Map<Integer,Long> map = new HashMap<>();

    static long fib(int x){
        if (map.containsKey(x)) return map.get(x);
        long y;
        if(x<=1) y=1;
        else y=fib(x-1)+fib(x-2);
        map.put(x,y);
        return y;
    }
    public static void main(String[] args) {
        System.out.println(fib(100));
    }
}