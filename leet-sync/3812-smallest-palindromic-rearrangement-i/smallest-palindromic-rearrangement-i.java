class Solution {
    public String smallestPalindrome(String s) {
        if (s.length() == 1) {
            return s;
        }

        int[] freq = new int[26];
        char odd = '1';

        for (char c : s.toCharArray()) {
            int charToInt = (int) (c - 'a');
            freq[charToInt]++;
        }

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < 26; i++) {
            if (freq[i] % 2 != 0) {
                odd = (char) (i + 'a');
                for (int j = 1; j <= freq[i] / 2; j++) {
                    sb.append((char) (i + 'a'));
                }
            }

            if (freq[i] % 2 == 0 && freq[i]!=0) {
                for (int j = 1; j <= freq[i] / 2; j++) {
                    sb.append((char) (i + 'a'));
                }
            }
        }

        int l = sb.length() - 1;

        if (odd != '1') {
            sb.append(odd);
        }

        for (int i = l; i != -1; i--) {
            sb.append(sb.charAt(i));
        }

        String ans = sb.toString();
        return ans;
    }
}