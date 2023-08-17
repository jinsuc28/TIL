# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root):
        self.cumSum = 0
        def dfs(node):
            if node:
                dfs(node.right)
                self.cumSum += node.val
                node.val = self.cumSum
                dfs(node.left)
        dfs(root)
        return root
    

# 인스턴스 변수로 누적합할 변수를 선언후 dfs로 오른쪽 끝 leaf 노드부터 순회하면서 연산 진행