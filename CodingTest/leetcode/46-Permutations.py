class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        if len(nums) == 1:
            return [nums]
        res_len = len(nums)
        skip_num = []
        res = []

        def dfs(i, nums, skip_num):
            if len(i) == res_len:
                res.append(i)
                return

            for num in nums:
                if num in skip_num:
                    pass
                else:
                    dfs(i + [num], nums, skip_num + [num])

        dfs([], nums, skip_num)

        return res