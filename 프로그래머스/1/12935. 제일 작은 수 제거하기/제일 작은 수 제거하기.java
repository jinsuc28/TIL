import java.util.Collections;
import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;


class Solution {
    public int[] solution(int[] arr) {
        
        List<Integer> list = new ArrayList<>();
        int min = 0;
        
        if (arr.length ==1){
            return new int[]{-1}; 
        }
        
        for (int i=0; i<arr.length; i++){
            if (i==0){
                min = arr[i];
            }
            if(i != 0 && arr[i] < min){
                min = arr[i];
            }
            
        }
        
        for (int i=0; i<arr.length; i++){
            if (arr[i] != min){
                list.add(arr[i]);
            }
        }
        
        int[] answer = new int[list.size()];
        for(int i = 0; i<list.size(); i++){
            answer[i] = list.get(i);
        }
        
        
        return answer;
    }
}