


#Definition for singly-link list.
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy=ListNode()
        dummy.next=head
        slow=fast=dummy

        while fast and fast.next:
            fast=fast.next.next #Fast moves by 2 steps
            slow=slow.next #Slow moves by 1 steps

            if slow is fast:
                return True # if Slow==fast
        
        return False