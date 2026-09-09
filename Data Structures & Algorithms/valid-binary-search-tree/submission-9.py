class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # def dfs(node, low, high):
        #     if not node:
        #         return True
        #     if not (low < node.val < high):
        #         return False
        #     return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        
        # return dfs(root, float("-inf"), float("inf"))

        if not root:
            return True
        stack = [(root, float("-inf"), float("inf"))]
        while stack:
            curr, low, high = stack.pop()
            
            if not low < curr.val < high:
                return False

            if curr.left:
                stack.append((curr.left, low, curr.val))

            if curr.right:
                stack.append((curr.right, curr.val, high))


        return True

