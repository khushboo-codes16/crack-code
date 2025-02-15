from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        
        for i in range(numRows):
            row = [1] * (i + 1)  # Initialize row with 1s
            
            for j in range(1, i):  # Compute inner values
                row[j] = result[i - 1][j - 1] + result[i - 1][j]
            
            result.append(row)
        
        return result

# Example usage:
numRows = 5
sol = Solution()
print(sol.generate(numRows))
