# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symm(root1,root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val != root2.val:
                return False
            
            return symm(root1.left,root2.right) and symm(root1.right,root2.left)
        
        return symm(root,root)

A=TreeNode(1)
B=TreeNode(2)
C=TreeNode(2)
D=TreeNode(3)
E=TreeNode(4)
F=TreeNode(4)
G=TreeNode(3)

A.left = B
A.right = C
B.left = D
B.right = E
C.left=F
C.right=G

n=Solution()
print(n.isSymmetric(A)) 