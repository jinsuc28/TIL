class Solution {
    public String solution(String s) {
        String answer = "";
        int numIdx = 0;
        String str = "";
        
        for (int idx=0; idx<s.length(); idx++){
            str = "" + s.charAt(idx);
            if((numIdx ==0) && !(" ".equals(str))){
                numIdx = 1;
                answer += str.toUpperCase();
            } else{
                answer += str.toLowerCase();
                if (" ".equals(str)){
                    numIdx = 0;
                }
                
            }
        }
        
        return answer;
    }
}
