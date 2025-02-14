from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Dictionary to store the next greater element for each number in nums2
        next_greater = {}
        stack = []
        
        # Iterate through nums2 to determine the next greater elements
        for num in nums2:
            while stack and stack[-1] < num:
                smaller_num = stack.pop()
                next_greater[smaller_num] = num
            stack.append(num)
        
        # The remaining numbers in stack have no next greater element
        while stack:
            next_greater[stack.pop()] = -1
        
        # Map results for nums1 based on the precomputed next_greater dictionary
        return [next_greater[num] for num in nums1]
