from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        while cur and cur.next:
            if cur.val==cur.next.val:
                cur.next=cur.next.next
            else:
                cur=cur.next
        
        return head

Head=ListNode(1)
A=ListNode(1)
B=ListNode(2)
Head.next=A
A.next=B
n=Solution()
print(n.deleteDuplicates(Head).val)
