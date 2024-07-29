class Solution {
    public String solution(String[] seoul) {

        int Num = 0;
        for (String str : seoul){
            
            
            if ("Kim".equals(str)){
                break;
            }
            
            Num += 1;
        
        }
        return "김서방은 " + Num + "에 있다";
    }
}