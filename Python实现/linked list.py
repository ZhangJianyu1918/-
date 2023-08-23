from typing import Optional

class ListNode():
    def __init__(self, value:int) -> None:
        self.value:int = value
        self.next:Optional(ListNode) = None
    
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)

n1.next = n2
n2.next = n3
n3.next = n4

