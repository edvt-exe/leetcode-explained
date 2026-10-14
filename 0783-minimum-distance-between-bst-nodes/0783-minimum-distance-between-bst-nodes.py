# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode | None) -> int:
        def find_max(node):
            while node.right:
                node = node.right
            return node.val

        def find_min(node):
            while node.left:
                node = node.left
            return node.val

        minim = float('inf')
        def dfs(node):
            nonlocal minim
            if node is None:
                return

            rad = node.val
            if node.left:
                max_node = find_max(node.left)
                minim = min(minim, rad - max_node)

            if node.right:
                min_node = find_min(node.right)
                minim = min(minim, min_node - rad)

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return minim