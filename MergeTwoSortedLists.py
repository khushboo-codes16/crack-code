from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Dummy node to serve as the start of the merged list
        current = dummy  # Pointer to construct the merged list
        
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Append the remaining nodes from either list1 or list2
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        return dummy.next  # Return the merged list starting from the next node of dummy
