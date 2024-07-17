class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        for i in sorted(intervals, key=lambda x: x[0]):
            if merged and i[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], i[1])
            else:
                merged += [i]
        
        return merged
    
    # 정렬후 중첩된다면 두 리스트에서 마지막 max 값을 비교해 큰 값으로 merge하는 방식