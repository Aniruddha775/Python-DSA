from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        for i in range(len(nums)):
            h[nums[i]]=i
        for i in range(len(nums)):
            y=target-nums[i]
            if y in h and h[y]!=i:
                return [i,h[y]]
            
n=Solution()
print(n.twoSum([2,7,11,15],9))  