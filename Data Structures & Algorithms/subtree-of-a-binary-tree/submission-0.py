# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        r=root
        t=subRoot
        if not t:
            return True
        if not r:
            return False
        if self.SameTree(r,t):
            return True
        return (self.isSubtree(r.left,t) or self.isSubtree(r.right,t))

    def SameTree(self,r,t):
            if not r and not t:
                return True
            if r and t and r.val==t.val:
                return (self.SameTree(r.left,t.left) and self.SameTree(r.right,t.right))
            return False
        