class ReverseWords {
    public String reverseWords(String s) {
        String[] words = s.split(" ");
        return helper(words, 0).trim();
    }

    private String helper(String[] words, int index) {
        if (index == words.length) return "";

        String reversed = new StringBuilder(words[index]).reverse().toString();
        return reversed + " " + helper(words, index + 1);
    
    }
}