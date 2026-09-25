# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        node = root

        lh = self.geth(node.left)
        rh = self.geth(node.right)

        if abs(lh - rh) > 1 :
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def geth(self, root):

        if root is None:
            return 0

        return 1 + max(self.geth(root.left), self.geth(root.right))
        