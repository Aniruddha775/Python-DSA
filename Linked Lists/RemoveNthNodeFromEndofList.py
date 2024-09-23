# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
   def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        behind = ahead = dummy

        for _ in range(n + 1):
            ahead = ahead.next

        while ahead:
            behind = behind.next
            ahead = ahead.next

        behind.next = behind.next.next

        return dummy.next

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
print(n.removeNthFromEnd(Head,2).val) 
#Printing the list
curr=Head
while curr:
    print(curr.val)
    curr=curr.next