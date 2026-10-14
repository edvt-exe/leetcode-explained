# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode | None) -> int:
        minimum = root.val
        second = float('inf')

        def dfs(node):
            nonlocal second

            if node is None:
                return

            if minimum < node.val < second:
                second = node.val

            dfs(node.right)
            dfs(node.left)

        dfs(root)
        if second != float('inf'):
            return second
        return -1

