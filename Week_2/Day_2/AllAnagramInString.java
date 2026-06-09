class AllAnagramInString {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> result = new ArrayList<>();

        if (p.length() > s.length()) return result;

        int[] p_Count = new int[26];
        int[] window = new int[26];

        // Frequency of p
        for (char c : p.toCharArray()) {
            p_Count[c - 'a']++;
        }
        int p_len = p.length();

        // First window
        for (int i = 0; i < p_len; i++) {
            window[s.charAt(i) - 'a']++;
        }
        if (Arrays.equals(p_Count, window)) result.add(0);

        // Sliding window
        for (int i = p_len; i < s.length(); i++) {
            window[s.charAt(i) - 'a']++;       // add new character
            window[s.charAt(i - p_len) - 'a']--;   // remove old character
            if (Arrays.equals(p_Count, window)) result.add(i - p_len + 1);
        }
        return result;
        
    }
}