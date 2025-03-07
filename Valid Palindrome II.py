class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(sub: str, left: int, right: int) -> bool:
            while left < right:
                if sub[left] != sub[right]:
                    return False
                left += 1
                right -= 1
            return True

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                # Try skipping either left or right character
                return is_palindrome(s, left + 1, right) or is_palindrome(s, left, right - 1)
            left += 1
            right -= 1

        return True
