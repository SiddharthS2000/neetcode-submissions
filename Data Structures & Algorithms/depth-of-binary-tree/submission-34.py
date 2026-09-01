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

        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        return 1 + max(left_height, right_height)


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

        if root is None:
            return 0

        stack = [[root, 1]]
        sol = 0

        while stack:
            node, depth = stack.pop()
            if node.left:
                stack.append([node.left, depth + 1])

            if node.right:
                stack.append([node.right, depth + 1])


            sol = max(sol, depth)

        return sol

            