class Solution {
    public int solution(int n) {
        int numSum = 0;
        
        if (n==0){
            return 0;    
        }
        
        for(int i=1; i< n+1; i++){
            if(n%i == 0){
                numSum += i;
            }
        }
        
        return numSum;
    }
}