import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()  # Remove non-alphanumeric characters and convert to lowercase
        return s == s[::-1]  # Check if the string is the same when reversed
