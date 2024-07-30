class Solution {
    public int solution(int num) {
        
        if (num ==1 ){
            return 0;
        }
        
        int iterNum = 0;
        while (iterNum<500){
            iterNum +=1;
            
            if (num%2==0){
                num = num/2;
            } else if(num%2==1){
                num = (num*3) +1;
            }
            
            if (num ==1){
                break;
            }
        }
        
        System.out.println(num);
        if (iterNum ==500){
            return -1;
        } else{
            return iterNum;
        } 
    }
}