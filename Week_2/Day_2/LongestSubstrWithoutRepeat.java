class LongestSubstrWithoutRepeat {
    public int lengthOfLongestSubstring(String s) {
        int left = 0;
        int max_len = 0;

        Set<Character> window = new HashSet<>();
        for (int right =0; right < s.length(); right++) {
            char ch = s.charAt(right);

            while (window.contains(ch)) {
                window.remove(s.charAt(left));
                left++;
            }
            window.add(ch);
            max_len = Math.max(max_len, right - left + 1);
        }

        return max_len;
    }
}
        