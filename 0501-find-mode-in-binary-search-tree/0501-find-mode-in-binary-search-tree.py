# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode | None) -> list[int]:
        result = []
        prev = None
        count = 0
        max_count = 0
        def dfs(node):
            nonlocal prev, count, max_count
            if node is None:
                return

            dfs(node.left)
            if node.val == prev:
                count += 1
            else:
                count = 1

            if count > max_count:
                max_count = count
                result.clear()
                result.append(node.val)
            elif count == max_count:
                result.append(node.val)
            prev = node.val
            dfs(node.right)

        dfs(root)
        return result