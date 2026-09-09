# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []
        queue = collections.deque([root] if root else [])

        while queue:
            lvl = []
            q_length = len(queue)
            for i in range(q_length):
                node = queue.popleft()
                lvl.append(node.val)

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            ret.append(lvl)
            
        return ret