# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True

        node = root

        lh = self.geth(node.left)
        rh = self.geth(node.right)

        if abs(lh - rh) <= 1 and \
            (self.isBalanced(node.left)) and \
            (self.isBalanced(node.right)):
            return True

        return False

    def geth(self, root):

        if root is None:
            return 0

        node = root

        lh = self.geth(node.left)
        rh = self.geth(node.right)

        return max(lh, rh) + 1
        