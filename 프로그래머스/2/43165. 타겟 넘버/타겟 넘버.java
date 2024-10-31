class Solution {
    int last_idx = 0;    
    int target = 0;
    int answer = 0;
    int[] numbers;
    
    public int solution(int[] numbers, int target) {
        this.answer = 0;
        this.last_idx = numbers.length;
        this.target = target;
        this.numbers = numbers;
        
        dfs(0, 0);
        
        
        return this.answer;
    }
    
    public void dfs(int total, int idx){
        if (idx == this.last_idx){
            if (total == this.target){
                this.answer += 1;
            }
            return;
        }
        
        dfs(total - this.numbers[idx], idx+1);
        dfs(total + this.numbers[idx], idx+1);
    }
}