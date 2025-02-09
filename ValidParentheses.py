class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # Bracket ko temporarily rakhne ke liye stack
        mapping = {')': '(', '}': '{', ']': '['}  # Closing aur opening bracket ka mapping

        for char in s:
            # Agar character closing bracket hai
            if char in mapping:
                # Stack ke last element ko nikal kar check karte hain
                top_element = stack.pop() if stack else '#'
                # Agar match nahi hota, to invalid hai
                if mapping[char] != top_element:
                    return False
            else:
                # Agar opening bracket hai to stack me daal dete hain
                stack.append(char)

        # Agar stack empty hai to valid otherwise invalid
        return not stack
