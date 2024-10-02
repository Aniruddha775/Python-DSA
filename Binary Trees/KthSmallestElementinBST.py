from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
   def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count=[k]
        ans=[0]

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            if count[0]==1: 
                ans[0]=node.val
    
            count[0]=count[0]-1 #We are decrementing the value of k till k=1
            if count[0]>0:
                dfs(node.right)
        
        dfs(root)
        return ans[0]
A=TreeNode(3)
B=TreeNode(1)
C=TreeNode(4)
E=TreeNode(2)


A.left = B
A.right = C
B.right = E

n=Solution()
print(n.kthSmallest(A, 1))  