class Solution {
    public int[] solution(long n) {
        
        String nStr = "" + n;
        int[] answer = new int[nStr.length()];
        
        
        for (int i=0; i<nStr.length(); i++){
            answer[nStr.length()-i-1] = Integer.parseInt(""+nStr.charAt(i));
        }
        return answer;
    }
}