from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        l_wall=r_wall=0
        n=len(height)
        max_left=[0]*n
        max_right=[0]*n

        for i in range(n):
            j=-i-1
            max_left[i]=l_wall
            max_right[j]=r_wall
            l_wall=max(l_wall,height[i])
            r_wall=max(r_wall,height[j])
        
        summ=0
        for i in range(n):
            potential_water=min(max_left[i],max_right[i])
            summ+=max(0,potential_water-height[i])

        return summ
    
n=Solution()
print(n.trap([0,1,0,2,1,0,1,3,2,1,2,1]))