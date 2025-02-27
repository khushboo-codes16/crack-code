from typing import List

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        # Start with the set of the first list
        common_elements = set(nums[0])
        
        # Intersect with all other lists
        for arr in nums[1:]:
            common_elements.intersection_update(arr)
        
        # Return sorted list of common elements
        return sorted(common_elements)
