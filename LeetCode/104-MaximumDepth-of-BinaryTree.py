
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth = 0
        bfs_map = deque()
        bfs_map.append(root)

        while bfs_map:
            depth += 1
            
            for _ in range(len(bfs_map)):
                child_node = bfs_map.popleft()
                if None != child_node.left:
                    bfs_map.append(child_node.left)
                if None != child_node.right:
                    bfs_map.append(child_node.right)

        return depth