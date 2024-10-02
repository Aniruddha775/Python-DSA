from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_distance=[float('inf')]
        prev=[None]
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            if prev[0] is not None:
                min_distance[0]=min(min_distance[0],node.val-prev[0])
            
            prev[0]=node.val
            dfs(node.right)
        
        dfs(root)
        return min_distance[0]

A=TreeNode(4)
B=TreeNode(2)
C=TreeNode(6)
D=TreeNode(1)
E=TreeNode(3)
F=TreeNode(15)
G=TreeNode(7)

A.left = B
A.right = C
B.left = D
B.right = E

n=Solution()
print(n.getMinimumDifference(A))  