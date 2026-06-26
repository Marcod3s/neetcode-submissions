# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        self.Same = True

        def dfs(p,q):
            if not p and not q:
                return True
            if not p and q:
                self.Same = False
                return self.Same
            if not q and p:
                self.Same = False
                return self.Same

            Left = dfs(p.left, q.left)
            Right = dfs(p.right,q.right)

            if p.val != q.val:
                self.Same = False
            return 
        
        dfs(p,q)
        
        return self.Same