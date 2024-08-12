class Solution {
    public String solution(String s) {
        int strLength = s.length();
        
        if (strLength%2==0){
            return s.substring(strLength/2 -1, strLength/2 +1);
        } else{
            return  s.substring(strLength/2, strLength/2+1);
        }

    }
}