import heapq
from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x,y):
            return x**2+y**2 # getting the eucledian distance
        
        heap=[]
        for x,y in points:
            d=dist(x,y)
            if len(heap)<k:
                heapq.heappush(heap,(-d,x,y)) #for max heap we use -d
            else:
                heapq.heappushpop(heap,(-d,x,y))
        
        return [(x,y) for d,x,y in heap]

n=Solution()
print(n.kClosest([[1,3],[-2,2]],1))  
