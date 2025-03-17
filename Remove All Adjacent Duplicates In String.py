class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()  # Remove adjacent duplicate
            else:
                stack.append(char)  # Keep the character if no duplicate
        
        return "".join(stack)
