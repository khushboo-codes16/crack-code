from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        
        for log in logs:
            if log == "../":
                if depth > 0:
                    depth -= 1
            elif log == "./":
                continue
            else:
                depth += 1
        
        return depth
    
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        
        return dummy.next
        
