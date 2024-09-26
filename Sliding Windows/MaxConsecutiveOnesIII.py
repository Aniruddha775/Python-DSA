from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n=len(nums)
        l=0
        max_w=0
        nums_zero=0
        
        for r in range(n):
            if nums[r] ==0:
                nums_zero+=1
            
            while nums_zero > k:
                if nums[l]==0:
                    nums_zero-=1
                l+=1
            
            window=r-l+1
            max_w=max(max_w,window)
        
        return max_w

n=Solution()
print(n.longestOnes([1,1,1,0,0,0,1,1,1,1,0],2))