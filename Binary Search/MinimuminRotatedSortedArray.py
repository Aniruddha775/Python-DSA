from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        l=0
        r=n-1

        while l<r:
            m=l+(r-l)//2
            if nums[m]>nums[r]:
                l=m+1
            else:
                r=m
        return nums[l] #or we can return nums[r] as in the end l==r
    
n=Solution()
print(n.findMin([4,5,6,7,0,1,2])) 