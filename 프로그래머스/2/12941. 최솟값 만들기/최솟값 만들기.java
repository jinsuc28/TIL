import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

class Solution{
    public int solution(int []A, int []B){
        int answer = 0;
        List<Integer> AList = new ArrayList<>();
        List<Integer> BList = new ArrayList<>();
        
        for (int i:A){
            AList.add(i);
        }
        
        for (int i:B){
            BList.add(i);
        }
        
        Collections.sort(AList,Collections.reverseOrder());
        Collections.sort(BList);
        
        
        int loopNum = AList.size();
        for (int i=0; i<loopNum; i++){
            answer += AList.get(i) * BList.get(i);
            // answer += Collections.max(AList) * Collections.min(BList);
            // AList.remove(Collections.max(AList));
            // BList.remove(Collections.min(BList));
        }
        
        
        return answer;
    }
}