from collections import deque
from typing import Optional,List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return None
        
        queue = deque()
        queue.append(root)
        ans = []
        
        while queue:
            level = []
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                level.append(node.val)

                if node.left: queue.append(node.left)                
                if node.right: queue.append(node.right)
            
            ans.append(level)

        return ans

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
print(n.levelOrder(A))