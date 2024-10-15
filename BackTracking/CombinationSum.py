from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans,sol=[],[]
        n=len(candidates)

        def backtrack(i,curr_sum):
            if curr_sum==target:
                ans.append(sol[:])
                return
            
            if curr_sum>target or i==n:
                return
            
            sol.append(candidates[i])
            backtrack(i,curr_sum+candidates[i]) #considering the same number for duplicates (left tree)
            sol.pop()
            backtrack(i+1,curr_sum) #not considering the same number (right tree)
        
        backtrack(0,0)
        return ans

n=Solution()
print(n.combinationSum([2,3,6,7],7))