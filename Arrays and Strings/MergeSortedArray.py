from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        x,y=m-1,n-1

        for z in range(m+n-1,-1,-1):
            if x<0:
                nums1[z]=nums2[y]
                y-=1
            elif y<0:
                break
            elif nums1[x]>nums2[y]:
                nums1[z]=nums1[x]
                x-=1
            else:
                nums1[z]=nums2[y]
                y-=1
        
n1=Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n=3
n1.merge(nums1, m, nums2, n) 
print(nums1)