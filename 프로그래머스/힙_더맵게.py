import heapq

def solution(scovile, k):
    heapq.heapify(scovile)
    cnt = 0
    
    while len(scovile) >= 2:
        min_1 = heapq.heappop(scovile)
        min_2 = heapq.heappop(scovile)
        heapq.heappush(scovile, min_1+min_2*2)
        cnt += 1
        
        if scovile[0] >= k:
            break
        
    if scovile[0] < k:
        cnt = -1
    
    return cnt