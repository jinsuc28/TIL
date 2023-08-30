class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums) # nums를 한번에 minheap 만들기

        for _ in range(len(nums) - k):
            heapq.heappop(nums)

        return heapq.heappop(nums)