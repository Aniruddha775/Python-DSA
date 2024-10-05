import heapq
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap=[]

        for num in nums:
            if len(min_heap)<k:
                heapq.heappush(min_heap,num) #Creating a min heap till k no. of elements
            else:
                heapq.heappushpop(min_heap,num) #Pushing one element and popping the smallest element when the heap is more than k
        
        return min_heap[0]

n=Solution()
print(n.findKthLargest([3,2,1,5,6,4],2))