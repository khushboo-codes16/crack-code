class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        prev = None

        # Find the middle of the linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the list
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # Compare both halves
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
