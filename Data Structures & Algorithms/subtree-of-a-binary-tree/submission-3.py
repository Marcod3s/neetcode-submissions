# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.Same = False

        if not subRoot:
            return True
        if not root:
            return False 
        if self.checkSame(root,subRoot):
            return True

        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

    def checkSame(self, curr, sub):
        if not curr and not sub:
            return True
        
        if curr and sub and curr.val == sub.val:
            return self.checkSame(curr.left, sub.left) and self.checkSame(curr.right, sub.right)
