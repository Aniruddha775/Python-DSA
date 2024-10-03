from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid(node,minn,maxx):
            if not node:
                return True
            
            if node.val<=minn or node.val>=maxx:
                return False
            
            return is_valid(node.left,minn,node.val) and is_valid(node.right,node.val,maxx) #For left we change the max to the current node and for the right we change min to current Node
        
        return is_valid(root,float('-inf'),float('inf'))

A=TreeNode(2)
B=TreeNode(1)
C=TreeNode(3)


A.left = B
A.right = C


n=Solution()
print(n.isValidBST(A))