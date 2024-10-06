from typing import List, Optional
import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]

        for i,node in enumerate(lists): #We build a heap using the first head reference from each lists
            if node:
                heapq.heappush(heap,(node.val,i,node)) #we are using i as if node.val is same then it can be identified by index i
        
        D=ListNode()
        curr=D

        while heap:
            val,i,node=heapq.heappop(heap) #We pop the minimum value from heap
            curr.next=node
            curr=node
            node=node.next
            if node:
                heapq.heappush(heap,(node.val,i,node)) # we push the next reference node to the heap
        
        return D.next

