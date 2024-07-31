class Solution {
    public int solution(int[] absolutes, boolean[] signs) {
        int answer = 0;
        int arrLength = absolutes.length;
        
        for(int i=0; i<arrLength; i++){
            if (signs[i] == true){
                answer += absolutes[i];
            } else{
                answer += absolutes[i]*-1;
            }
        }
        
        
        return answer;
    }
}