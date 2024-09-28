# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left=self.maxDepth(root.left)
        right=self.maxDepth(root.right)
        return 1 + max(left,right) 
    
A=TreeNode(3)
B=TreeNode(9)
C=TreeNode(20)
D=TreeNode()
E=TreeNode()
F=TreeNode(15)
G=TreeNode(7)

A.left = B
A.right = C
B.left = D
B.right = E
C.left=F
C.right=G

n=Solution()
print(n.maxDepth(A)) 