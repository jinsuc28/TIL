class Solution {
    boolean solution(String s) {
        int sCount = 0;
        int yCount = 0;
        
        for (int i=0; i<s.length(); i++){
            if ('p' == s.charAt(i) || 'P'==s.charAt(i)){
                sCount += 1;
            }
            if ('y' == s.charAt(i) || 'Y' == s.charAt(i)){
                yCount += 1;
            }
        }
        // charAt return -> char 타입
        // equals는 char타입 비교 불가, 객체에 대해서만 가능
        
        if (sCount == yCount){
            return true;
        } else{
            return false;
        }
    }
}