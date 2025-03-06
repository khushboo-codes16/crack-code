class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        balance = 0  # Keeps track of open parentheses count

        for char in s:
            if char == '(':
                if balance > 0:  # Only add if it's not an outer '('
                    result.append(char)
                balance += 1
            else:  # char == ')'
                balance -= 1
                if balance > 0:  # Only add if it's not an outer ')'
                    result.append(char)

        return ''.join(result)
