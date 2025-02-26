# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        num = 0
        while head:
            num = num * 2 + head.val  # Left shift and add current digit
            head = head.next
        return num
