# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [True, 0]

            left, right = dfs(node.left),dfs(node.right)
            
            # if both subtrees are balanced and height diff is < 2
            balanced = bool(left[0] and right[0] and abs(left[1] - right[1]) <= 1)
            return [balanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]


        def dfs(node):
            if node is None:
                return (True, 0)

            left_height, right_height = dfs(node.left), dfs(node.right)
            is_balanced = left_height[0] and right_height[0] and abs(left_height[1] - right_height) < 2

            return (is_balanced, 1+max(left[1], right[1]))