class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxValueOnPath):
            if node is None:
                return 0

            # A node is "good" if it's >= all values seen so far on the path
            good_count = 1 if node.val >= maxValueOnPath else 0

            # Update the max value for the path including this node
            newMax = max(maxValueOnPath, node.val)

            # Count good nodes in left and right subtrees
            good_count += dfs(node.left, newMax)
            good_count += dfs(node.right, newMax)

            return good_count

        return dfs(root, root.val)
