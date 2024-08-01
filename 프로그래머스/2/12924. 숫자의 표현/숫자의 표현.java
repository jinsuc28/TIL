class Solution {
    public int solution(int n) {
        int answer = 0;
        int fristNum = 0;
        int startNum =1;
        
        while (startNum<=n){
            int sumNum = 0;
            for (int i=startNum; i<=n; i++){
                sumNum += i;
                if(sumNum == n){
                    answer +=1;
                    break;
                }
                if(sumNum>n){
                    break;
                }
            }
            startNum +=1;
            
        }
        
        return answer;
    }
}