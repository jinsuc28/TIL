import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        
        
        Stack<Integer> stack = new Stack<>();
        int beforeNum = arr[0];
        stack.push(arr[0]);
        
        for (int i=1; i<arr.length; i++){
            
            if(arr[i] != beforeNum){
                stack.push(arr[i]);
            }
            beforeNum = arr[i];
        }
        
        
        int[] answer = new int[stack.size()];
        for (int n=stack.size()-1; n>=0; n--){
            answer[n] = stack.pop();
        }
        

        return answer;
    }
}