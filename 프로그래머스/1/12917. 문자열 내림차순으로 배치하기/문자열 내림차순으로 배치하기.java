import java.util.Arrays;

class Solution {
    public String solution(String s) {
        char[] strArray = s.toCharArray();
        Arrays.sort(strArray);
        
        String str = new String(strArray);
        
        return new StringBuilder(str).reverse().toString();
    }
}