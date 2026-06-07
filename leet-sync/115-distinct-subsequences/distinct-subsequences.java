class Solution {

    HashMap<String, Long> map = new HashMap<>();

    public int numDistinct(String s, String t) {
        return (int) dfs(0, 0, s, t);
    }

    public long dfs(int i, int j, String s, String t) {

        if (j == t.length()) {
            return 1;
        }

        if (i == s.length()) {
            return 0;
        }

        String key = i + ";" + j;

        if (map.containsKey(key)) {
            return map.get(key);
        }

        long ans;

        if (s.charAt(i) == t.charAt(j)) {

            ans =
                dfs(i + 1, j + 1, s, t)
                +
                dfs(i + 1, j, s, t);

        } else {

            ans = dfs(i + 1, j, s, t);
        }

        map.put(key, ans);

        return ans;
    }
}