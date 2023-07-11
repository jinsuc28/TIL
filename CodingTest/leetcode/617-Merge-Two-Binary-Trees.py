# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # 재귀로 풀기
        if root1 and root2: # 둘중 하나라도 None 없을 때만
            node = TreeNode(val = root1.val + root2.val)
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)

            return node
        else:
            return root1 or root2

"""
TreeNode 클래스를 선언하면서 동시에 인스턴스 변수로 두개 트리의
val 값을 합하며 둘 중 하나만 None이면 None 아닌 값을 내며
둘다 None 일경우 None 을 내도록 함(root1 or root2)
다시말해 None 채워진 부분까지 탐색후 백트래킹을 통해서 left, right 순으로 채워지며 트리를 완성시킴
"""