# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q=collections.deque()
        q.append(root)
        res=[]
        while q:
            qLen=len(q)
            rightSide=None
            for i in range(qLen):
                Node=q.popleft()
                if Node:
                    rightSide=Node
                    q.append(Node.left)
                    q.append(Node.right)
            if rightSide:
                res.append(rightSide.val)
        return res
                    
        
        