import java.util.Collections;
import java.util.List;
import java.util.ArrayList;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        List<Integer> list = new ArrayList<>();
        
        for (int num : arr){
            if (num % divisor == 0){
                list.add(num);
            }
        }
        if (list.size() == 0){
            return new int[]{-1};
        }
        
        Collections.sort(list);
        
        int[] answer = new int[list.size()];
        for (int idx=0; idx<list.size(); idx++){
            answer[idx] = list.get(idx);
        }
        
        return answer;
    }
}

