# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 클래스 변수 선언
    result: int = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode):
            if node is None:
                return 0

            # 마지막 left, right 가 None부터 백트래킹 시작
            left = dfs(node.left) # 초기 0
            right = dfs(node.right)

            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0 
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0
            
            self.result = max(self.result, left + right) # left + right 둘다 더함

            return max(left, right) # path 이기 때문에 left, right 중 하나만 return

        dfs(root)
        return self.result
        # 왼쪽 리프노드부터 순차적으로 계산됨 

'''
dfs와 TreeNode의 이어진 노드가 없는 경우 None 값인 것을 이용해
백트래킹해서 푸는 문제
'''