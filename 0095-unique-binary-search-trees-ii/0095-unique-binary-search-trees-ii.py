# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> list[TreeNode | None]:
        def build(left, right):
            if left > right:
                return [None]

            result = []

            for root in range(left, right + 1):
                left_trees = build(left, root - 1)
                right_trees = build(root + 1, right)

                for left_tree in left_trees:
                    for right_tree in right_trees:
                        node = TreeNode(root)
                        node.left = left_tree
                        node.right = right_tree
                        result.append(node)

            return result

        return build(1, n)