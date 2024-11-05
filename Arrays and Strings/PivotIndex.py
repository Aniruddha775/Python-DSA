from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalsum=sum(nums)

        leftsum=0
        for i in range(len(nums)):
            if leftsum==totalsum-leftsum-nums[i]:
                return i
            leftsum+=nums[i]
        
        return -1

n=Solution()

print(n.pivotIndex([1, 7, 3, 6, 5, 6])) # Output: 3
