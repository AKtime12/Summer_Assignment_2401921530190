class DecodeString {
    private int index = 0;
    public String decodeString(String s) {
        StringBuilder result = new StringBuilder();
        int num = 0;
        while (index < s.length()) {
            char ch = s.charAt(index);
            if (Character.isDigit(ch)) {
                num = num * 10 + (ch - '0');
                index++;
            } 
            else if (ch == '[') {
                index++; // skip '['
                String decoded = decodeString(s);

                while (num-- > 0) {
                    result.append(decoded);
                }
                num = 0;
            } 
            else if (ch == ']') {
                index++; // skip ']'
                return result.toString();
            } 
            else {
                result.append(ch);
                index++;
            }
        }
        return result.toString();
    }
}