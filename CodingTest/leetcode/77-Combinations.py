class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        if n == 1:
            return [[n]]
        
        if n == k:
            return [[num for num in range(1, n+1)]]

        num_list = [i for i in range(1,n+1)]
        res = []

        def recursive(num_list, com):
            
            if k == len(com):
                res.append(com)
                return 

            for idx, num in enumerate(num_list):

                recursive(num_list[idx+1:], com + [num])
        
        recursive(num_list, [])

        return res