from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res,sol=[],[]

        def backtrack(i):
            if i==n:
                res.append(sol[:]) #copying the sol list to res
                return
            
            #dont pick nums (Left tree)
            backtrack(i+1)

            #pick nums(right tree)
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop() #we are popping it for backtracking and we are popping so that there are no duplicates
        
        backtrack(0) #starting at index=0
        return res

n=Solution()
print(n.subsets([1,2,3]))