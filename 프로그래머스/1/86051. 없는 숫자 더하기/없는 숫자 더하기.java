class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        boolean b = false;
        
        for (int i=0; i<10; i++){
            b = false;
            for (int num:numbers){
                if (num == i){
                    b =true;
                }
            }
            if (b==false){
                answer +=i;
            }
        }
        
        return answer;
    }
}