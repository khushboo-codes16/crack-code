from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Initialize the row with 1s, since the first and last elements are always 1
        row = [1] * (rowIndex + 1)
        
        # Build the row from the back to the front
        for i in range(2, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                row[j] = row[j] + row[j - 1]
        
        return row

# Example usage:
solution = Solution()
print(solution.getRow(3))  # Output: [1, 3, 3, 1]
print(solution.getRow(0))  # Output: [1]
print(solution.getRow(1))  # Output: [1, 1]
