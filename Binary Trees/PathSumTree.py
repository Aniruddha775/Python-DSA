# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def has_sum(root,curr_sum):
            if not root:
                return False
            
            curr_sum+=root.val
            if not root.left and not root.right:
                return curr_sum==targetSum
            return has_sum(root.left,curr_sum) or has_sum(root.right,curr_sum)
        
        return has_sum(root,0)

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
print(n.hasPathSum(A,6)) 