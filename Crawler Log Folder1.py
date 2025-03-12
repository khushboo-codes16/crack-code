from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for log in logs:
            if log == "../":
                depth = max(0, depth - 1)  # Move up a level, but not below root
            elif log == "./":
                continue  # Stay in the same directory
            else:
                depth += 1  # Move to a child directory
        return depth
