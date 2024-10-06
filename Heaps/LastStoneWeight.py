import heapq
from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]=-stones[i] #For Max Heapify
        
        heapq.heapify(stones)

        while len(stones)>1:
            largest=heapq.heappop(stones)
            next_largest=heapq.heappop(stones)

            if largest!=next_largest:
                heapq.heappush(stones,largest-next_largest)
        
        if len(stones)==1:
            return -heapq.heappop(stones)
        else:
            return 0

n=Solution()
print(n.lastStoneWeight([2,7,4,1,8,1]))