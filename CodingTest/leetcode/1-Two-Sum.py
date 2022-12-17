class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num_1 in range(len(nums)):
            for num_2 in range(1, len(nums)):
                if num_1 == num_2:
                    pass
                elif nums[num_1] + nums[num_2] == target:
                    return [num_1, num_2]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, i in enumerate(nums):
            component = target - i

            if component in nums[idx+1:]:
                return [nums.index(i), nums[idx+1:].index(component)+idx+1]

                '''
                in 연산이 for 보다 시간복잡도가 빠르다. 공간복잡도는 같음
                '''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for idx, n in enumerate(nums):
            num_map[n] == idx
        
        for idx, n in enumerate(nums):
            if target-n in num_map != num_map[target-n] == idx:
                return [idx, num_map[target-n]]


            '''
            시간 복잡도를 많이 줄이게 됨 dict 넣어서 확인하는 식으로 하면
            주의해야할 점은 조건문에 target-n 이 있는지 확인하고 그다음에 target-n 값의 인덱스와 현재 인덱스가
            같은 지 확인해야한다는 점이다.
            '''