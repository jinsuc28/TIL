import java.util.List;
import java.util.ArrayList;

class Solution{
    public int solution(String s){
        List<String> list = new ArrayList<>();
        for (int idx = 0; idx < s.length(); idx++) {
            if (list.size() == 0) {
                list.add("" + s.charAt(idx));
                continue;
            }

            if (!list.get(list.size() - 1).equals("" + s.charAt(idx))) {
                list.add("" + s.charAt(idx));
            } else {
                list.remove(list.size() - 1);
            }
        }
        
        return (list.size() == 0 ? 1 : 0);
    }
}
//         int idx1=0;
//         for (int idx=0; idx<s.length(); idx++){
//             list.add("" + s.charAt(idx));
//         }
        
//         if (list.size()%2 ==1){
//             return 0;
//         }
        
//         while (true){
//             if (list.size()==1){
//                 return 0;
//             }
            
//             if (list.size()==0){
//                 return 1;
//             }
//             for (; idx1<list.size(); idx1++){
//                 if (idx1==list.size()-1){
//                     return 0;
//                 }
                
//                 if (list.get(idx1).equals(list.get(idx1+1))){
//                     list.remove(idx1);
//                     list.remove(idx1);
//                     if (idx1-1>=0){
//                         idx1 = idx1-1;
//                     }
                    
//                     break;
//                 }
//             }
//         }
        
        
        // return 0;
        
        
        
//         String First = "";
//         String Second = "";
        
//         while(true){
//             if (s.length() ==0){
//                 return 1;
//             }
            
//             for (int idx=0; idx<s.length(); idx++){
//                 if (idx == s.length()-1){
//                     return 0;
//                 }
                
//                 First = s.substring(idx, idx+1);
//                 Second = s.substring(idx+1, idx+2);
//                 if ((idx != 0) && (First.equals(Second))){
//                     s = s.substring(idx-1,idx) + s.substring(idx+2);
//                     break;
//                 }
//                 if ((idx ==0) && (First.equals(Second))){
//                     s = s.substring(idx+2);
//                     break;
//                 }
                
                    
//             }
            
//         }
//     }
// }


