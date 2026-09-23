# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        total_tilt = 0

        def subtree_sum(node):
            nonlocal total_tilt

            if node is None:
                return 0

            left_sum = subtree_sum(node.left)
            right_sum = subtree_sum(node.right)

            tilt = abs(left_sum - right_sum)
            total_tilt += tilt

            return node.val + left_sum + right_sum

        subtree_sum(root)

        return total_tilt