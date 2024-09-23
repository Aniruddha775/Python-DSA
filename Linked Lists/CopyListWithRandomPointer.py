from typing import Optional
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
        
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        
        curr=head
        old_to_new={}

        while curr:
            node=Node(x=curr.val)
            old_to_new[curr]=node
            curr=curr.next    
        curr=head
        while curr:
            new_node=old_to_new[curr]
            new_node.next=old_to_new[curr.next] if curr.next else None
            new_node.random=old_to_new[curr.random] if curr.random else None
            curr=curr.next
        
        return old_to_new[head]

Head=Node(1)
A=Node(2)
B=Node(3)
C=Node(4)
D=Node(5)
Head.next=A
A.next=B    
B.next=C
C.next=D
n=Solution()
print(n.copyRandomList(Head))
#Printing the list
curr=Head
while curr:
    print(curr.val)
    curr=curr.next