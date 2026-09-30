from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = deque([root])
        while q:
            curr = []
            n = len(q)

            for _ in range(n):
                node = q.popleft()
                if not node:
                    continue
                curr.append(node.val)
                q.append(node.left)
                q.append(node.right)

            res.append(curr)
        res.pop()
        return res

        