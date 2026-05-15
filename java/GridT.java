import java.util.HashMap;
import java.util.Map;
public class GridT{
    static Map<Integer,Map<Integer,Integer>> map =new HashMap<>();

    static int gridTraveller(int x, int y){
        if(x==0 || y==0) return 0;
        if(x==1 || y==1) return 1;
        if(map.containsKey(x)&& map.get(x).containsKey(y)){
            return map.get(x).get(y);
        }
        int result=gridTraveller(x-1, y)+gridTraveller(x, y-1); 
        map.putIfAbsent(x,new HashMap<>());
        map.get(x).put(y,result);
        return result;
    }
    public static void main(String[] args) {
        System.out.println(gridTraveller(2,2 ));
        
    }
}