# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.res = [root.val]
        self.dfs(root)
        return self.res[0]

    def dfs(self, root):

        if not root:
            return 0

        leftmax = max(0, self.dfs(root.left))
        rightmax = max(0, self.dfs(root.right))

        self.res[0] = max(self.res[0], root.val + leftmax + rightmax)

        return root.val + max(leftmax, rightmax)
        