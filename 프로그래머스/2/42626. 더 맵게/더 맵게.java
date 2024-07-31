import java.util.PriorityQueue;

class Solution {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        Integer Num1 = 0;
        Integer Num2 = 0;
        int Count = 0;
        int numSum = 0;
        
        for (int idx=0; idx<scoville.length; idx++){
            minHeap.offer(scoville[idx]);
        }
        
        
        
        while(true){
            if (minHeap.size()<2 && minHeap.peek()<K){
                return -1;
            } else if (minHeap.peek()>=K){
                return Count;
            }
            
            Num1 = minHeap.poll();
            Num2 = minHeap.poll();
            
            minHeap.offer(Num1 + (Num2*2));
            Count++;
        }
    }
}