# https://leetcode.com/problems/find-closest-number-to-zero/description/

from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest=nums[0]
        for i in nums:
            if abs(i)<abs(closest):
                closest=i
        if closest<0 and abs(closest) in nums:
            return abs(closest)
        return closest

a=Solution()
print(a.findClosestNumber([-4,-2,1,4,8])) 