# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        curr=dummy
        summ=carry=0
        while l1 or l2 or carry!=0:
            summ=carry
            if l1:
                summ+=l1.val
                l1=l1.next
            if l2:
                summ+=l2.val
                l2=l2.next
            
            carry=summ // 10
            summ= summ % 10
            curr.next=ListNode(summ)
            curr=curr.next
        
        return dummy.next

n=Solution()
l1=ListNode(2)
l1.next=ListNode(4)
l1.next.next=ListNode(3)
l2=ListNode(5)
l2.next=ListNode(6)
l2.next.next=ListNode(4)
print(n.addTwoNumbers(l1,l2).val)