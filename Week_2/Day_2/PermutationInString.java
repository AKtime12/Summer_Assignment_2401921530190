class PermutationInString {
    public boolean checkInclusion(String s1, String s2) {
        int n1 = s1.length();

        if (s1.length() > s2.length()) return false;
        int[] need = new int[26];
        int[] window = new int[26];

        // Count freq's in s1
        for (char c : s1.toCharArray()) {
            need[c - 'a']++;
        }

        // Building first window
        for (int i = 0; i < n1; i++) {
            window[s2.charAt(i) - 'a']++;
        }
        if (matches(need, window)) return true;

        // Sliding the window
        for (int i = n1; i < s2.length(); i++) {
            window[s2.charAt(i) - 'a']++;       // add new character
            window[s2.charAt(i - n1) - 'a']--;   // remove old character

            if (matches(need, window)) return true;
        }

        return false;
    }

    private boolean matches(int[] a, int[] b) {
        for (int i = 0; i < 26; i++) {
            if (a[i] != b[i]) return false;
        }
        return true;
        
    }
}