from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans,sol=[],[]

        def backtrack(openn,close):
            if len(sol)==2*n:
                ans.append(''.join(sol))
                return
            
            if openn<n:
                sol.append('(')
                backtrack(openn+1,close) #go down the left tree of open brackets
                sol.pop()
            
            if openn>close: 
                sol.append(')')
                backtrack(openn,close+1) #go down the right tree of closing brackets
                sol.pop()
        
        backtrack(0,0)
        return ans

n=Solution()
print(n.generateParenthesis(3))  
