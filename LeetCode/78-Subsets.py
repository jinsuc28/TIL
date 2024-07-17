class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:

        res = []
        subset = []

        def dfs(i):
            # if nums index exceed return
            if i == len(nums):
                res.append(subset.copy()) # if not use copy() than return init subset, ex) []
                return
            
            subset.append(nums[i])
            # select nums element
            dfs(i + 1)
            
            # not select nums element
            subset.pop()
            dfs(i + 1)

        dfs(0)

        return res
            

if "__main__"==__name__:
    nums = [1,2,3]
    print(Solution().subsets(nums))