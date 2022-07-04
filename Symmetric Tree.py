# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSym(left, right):
            if left and right:
                if left.val == right.val:
                    return isSym(left.left, right.right) and isSym(left.right, right.left)
            elif not left and not right:
                return True
            return False
        return isSym(root.left, root.right)
