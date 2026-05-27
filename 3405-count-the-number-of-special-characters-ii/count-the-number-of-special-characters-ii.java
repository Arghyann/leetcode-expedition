class Solution {
    public int numberOfSpecialChars(String word) {
        int count = 0;

        for (char c = 'A'; c <= 'Z'; c++) {

            int firstUpper = -1;
            int lastLower = -1;

            // scan whole string
            for (int i = 0; i < word.length(); i++) {
                char ch = word.charAt(i);

                if (ch == c && firstUpper == -1) {
                    firstUpper = i;
                }

                if (ch == Character.toLowerCase(c)) {
                    lastLower = i;
                }
            }

            if (lastLower != -1 &&
                firstUpper != -1 &&
                lastLower < firstUpper) {
                count++;
            }
        }

        return count;
    }
}