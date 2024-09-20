from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        ans=[0]*n
        stk=[]

        for i,t in enumerate(temperatures):
            while stk and stk[-1][0]<t:
                stk_t,stk_i=stk.pop()
                ans[stk_i]=i-stk_i
            
            stk.append((t,i))
        
        return ans

n=Solution()
print(n.dailyTemperatures([73,74,75,71,69,72,76,73]))