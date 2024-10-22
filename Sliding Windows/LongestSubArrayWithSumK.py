from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        max_length=float('-inf')
        l=0
        summ=0

        for r in range(len(nums)):
            summ+=nums[r]

            while summ>=target:
                summ-=nums[l]
                max_length=max(max_length,r-l+1)
                l+=1
        
        return max_length if max_length<float('inf') else 0

n=Solution()
print(n.minSubArrayLen(15, [10, 5, 2, 7, 1, 9])) #