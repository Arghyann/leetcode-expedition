import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Cansum {
    static Map<String, Integer> map = new HashMap<>();

    static int cansum(int x, int[] y) {
        if (x == 0) return 1;
        if (x < 0) return 0;

        String key = Arrays.toString(y) + ":" + x;

        if (map.containsKey(key)) {
            return map.get(key);
        }

        int tot = 0;

        for (int i = 0; i < y.length; i++) {
            int[] newArr = new int[y.length - 1];
            int j = 0;

            for (int t = 0; t < y.length; t++) {
                if (t == i) continue;

                newArr[j] = y[t];
                j++;
            }

            tot += cansum(x - y[i], newArr);
        }

        map.put(key, tot);
        System.out.println(tot + ":" + key );
        return tot;
    }

    public static void main(String[] args) {
        System.out.println(cansum(7, new int[]{}));
    }
}