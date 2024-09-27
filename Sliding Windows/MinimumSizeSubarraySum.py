from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length=float('inf')
        l=0
        summ=0

        for r in range(len(nums)):
            summ+=nums[r]

            while summ>=target:
                summ-=nums[l]
                min_length=min(min_length,r-l+1)
                l+=1
        
        return min_length if min_length<float('inf') else 0

n=Solution()
print(n.minSubArrayLen(7, [2,3,1,2,4,3])) #