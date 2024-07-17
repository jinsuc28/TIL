# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        val_list = []

        def dfs(tree):
            if tree is None:
                return

            val_list.append(tree.val)
            dfs(tree.left)
            dfs(tree.right)
        
        dfs(root)

        valsum = 0
        for i in val_list:
            if i >= low and i <= high:
                valsum += i

        return valsum
    
# 리스트에 val 값들 담아두고 범위 안이면 합치는 방식으로 품.