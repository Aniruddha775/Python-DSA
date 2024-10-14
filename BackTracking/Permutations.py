from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans,sol=[],[]

        def backtrack():
            if len(sol)==n:
                ans.append(sol[:])
                return
            for i in nums:
                if i not in sol: #we dont want to append the numbers which we have already picked
                    sol.append(i)
                    backtrack()
                    sol.pop()
        
        backtrack()
        return ans

n=Solution()
print(n.permute([1,2,3]))