from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced=[True]

        def height(root):
            if not root:
                return 0
            
            left_height=height(root.left)
            if balanced[0] is False:
                return 0
            right_height=height(root.right)

            if abs(left_height-right_height)>1:
                balanced[0]=False
                return 0
            
            return 1 + max(left_height,right_height)
        
        height(root)
        return balanced[0]

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
C.left = F
C.right = G

n=Solution()
print(n.isBalanced(A)) 