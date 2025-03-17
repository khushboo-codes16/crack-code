from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []  # Monotonic stack to keep track of indices
        result = prices[:]  # Copy of prices to store final prices
        
        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                index = stack.pop()
                result[index] -= price
            stack.append(i)
        
        return result
