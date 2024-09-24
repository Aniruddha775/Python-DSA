from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        min_index = l

        if min_index == 0:
            l, r = 0, n - 1 # then the array is not rotated
        elif target >= nums[0] and target <= nums[min_index - 1]:
            l, r = 0, min_index - 1
        else:
            l, r = min_index, n - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1
n=Solution()
nums = [4,5,6,7,0,1,2]
target = 1
print(n.search(nums,target))