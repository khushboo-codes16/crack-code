class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        
        # Compute the sum of the first B elements
        current_sum = sum(A[:B])
        max_sum = current_sum
        
        # Sliding window: Take elements from the end and remove elements from the start
        for i in range(1, B + 1):
            current_sum = current_sum - A[B - i] + A[n - i]
            max_sum = max(max_sum, current_sum)
        
        return max_sum
