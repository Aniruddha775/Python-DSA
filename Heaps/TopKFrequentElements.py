from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        n=len(nums)
        buckets=[0]*(n+1) # we are taking n+1 as a number can have freq 0
        for c in nums:
            if c in count:
                count[c]+=1
            else:
                count[c]=1
        
        for num,freq in count.items():
            if buckets[freq]==0:
                buckets[freq]=[num]
            else:
                buckets[freq].append(num)
        ret=[] #for return the final list in reverse order
        for i in range(n,-1,-1):
            if buckets[i]!=0:
                ret.extend(buckets[i])
            if len(ret)==k:
                break
        
        return ret

#Using Heap   
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []

        for key, val in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, key))
            else:
                heapq.heappushpop(heap, (val, key))
        
        return [h[1] for h in heap]