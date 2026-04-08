# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(Node,maxValue):
            if not Node:
                return 0
            res=1 if Node.val>=maxValue else 0
            maxValue=max(maxValue,Node.val)
            res+=dfs(Node.left,maxValue)
            res+=dfs(Node.right,maxValue)
            return res
        return dfs(root,root.val)