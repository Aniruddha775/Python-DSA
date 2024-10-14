from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans,sol=[],[]
        def backtrack(x):
            if len(sol)==k:
                ans.append(sol[:])
                return
            
            nos_left=x
            still_need=k-len(sol)
            if nos_left>still_need: #then skip these numbers
                backtrack(x-1)
            
            sol.append(x)
            backtrack(x-1)
            sol.pop()

        backtrack(n)
        return ans

n=Solution()
print(n.combine(4,2))