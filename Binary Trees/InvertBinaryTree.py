# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.val)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        root.left,root.right=root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
    
A=TreeNode(4)
B=TreeNode(2)
C=TreeNode(7)
D=TreeNode(1)
E=TreeNode(3)
F=TreeNode(6)
G=TreeNode(9)

A.left = B
A.right = C
B.left = D
B.right = E
C.left=F
C.right=G

n=Solution()
n.invertTree(A)

#Printing the Tree
from collections import deque

def level_order(node):
  q = deque()
  q.append(node)

  while q:
    node = q.popleft()
    print(node)
    if node.left: q.append(node.left)
    if node.right: q.append(node.right)

level_order(A)

