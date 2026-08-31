# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        # if not root:
        #     return 0
        # q = deque([root])
        # depth = 0

        # while q:
        #     for i in range(len(q)):
        #         curr = q.popleft()
        #         if curr.left:
        #             q.append(curr.left)
        #         if curr.right:
        #             q.append(curr.right)
        #     depth += 1

        # return depth

        # if root is None:
        #     return 0

        # sol = 0
        # stack = [[root, 1]]
        # while stack:
        #     top, depth = stack.pop()
        #     if top.left:
        #         stack.append([top.left, depth + 1])
        #     if top.right:
        #         stack.append([top.right, depth + 1])
        #     sol = max(sol, depth)
        # return sol