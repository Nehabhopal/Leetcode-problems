# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        maxi = [float("-inf")]

        def solve(node):
            if node is None:
                return 0

            leftsum = solve(node.left)
            if leftsum < 0:
                leftsum = 0

            rightsum = solve(node.right)
            if rightsum < 0:
                rightsum = 0

            maxi[0] = max(maxi[0], leftsum + node.val + rightsum)

            return node.val + max(leftsum, rightsum)

        solve(root)
        return maxi[0]