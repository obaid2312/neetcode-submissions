# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        dia = [0]
        self.h(root, dia)
        return dia[0]

    def h(self, node, dia):

        if not node:
            return 0

        lh = self.h(node.left, dia)
        rh = self.h(node.right, dia)

        dia[0] = max(dia[0], lh + rh)

        return 1 + max(lh, rh)
        