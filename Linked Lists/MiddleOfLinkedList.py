# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head

        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        
        return slow
    
Head=ListNode(1)
A=ListNode(2)
B=ListNode(3)
C=ListNode(4)
D=ListNode(5)
Head.next=A
A.next=B    
B.next=C
C.next=D
n=Solution()
print(n.middleNode(Head).val) 