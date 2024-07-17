class Solution {
    boolean solution(String s) {

        int state = 0;
        
        if( (")".equals("" + s.charAt(0))) || ("(".equals("" + s.charAt(s.length()-1)))){
            return false;
        }
        
        for(int i=0; i<s.length(); i++){
            if((i>0) && (state==0) &&(")".equals("" + s.charAt(i)))){
                return false;
            }
            
            if ("(".equals("" + s.charAt(i))){
                ++state;
            }
            else{
                --state;
            }
        }

        return ( state == 0 ? true: false);
    
        
    }
}