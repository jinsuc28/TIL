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
//         String[] strArray = s.split(" ");
//         String str;
        
//         if (strArray.length ==0){
//             return s;
//         }
        
//         for (int arrIdx = 0; arrIdx<strArray.length; arrIdx++){
//             str = strArray[arrIdx];
//             for (int idx=0; idx<str.length(); idx++){
//                 // char c = str.charAt(idx);
//                 if (idx==0){
//                     answer += ("" + str.charAt(idx)).toUpperCase();
//                 } else{
//                     answer += ("" + str.charAt(idx)).toLowerCase();
//                 }
//                 // answer += ((String) c).toUpperCase();
//             }

            
//             if (arrIdx <strArray.length-1){
//                 answer += " ";
//             }
            
//         }
                
        return answer;
    }
}