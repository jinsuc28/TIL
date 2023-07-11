# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        queue = collections.deque([root])

        while queue:
            node = queue.popleft()

            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        
        return root
        # 위 풀이법은 파이썬의 참조 개념을 잘 활용하여서 풀이한 것 같다.
        # 예를 들어 node.left 리스트에 담고 node라는 변수로 하고 이 값을 node.right 바꿔주면
        # 이 node라는 변수는 이전 node.left 주소를 바인딩하였기 때문에 값이 변경되면 root 값이 바뀌는 것

class Solution2:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return None
        
        root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)

        return root

        # 일반적으로 재귀를 사용하여서 풀면 됨