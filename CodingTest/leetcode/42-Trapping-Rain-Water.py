class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        volume = 0 
        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]
        
        while left < right:
            left_max, right_max = max(left_max, height[left]), max(right_max, height[right])
            
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1 
                
        return volume


        '''
        어려웠음 이해가 잘안되었음 시간지난 다음 다시한번 풀어보자
        '''