class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        positive_v = 0
        negative_v = 0
         
        for num in A:
             if num > 0 :
                 positive_v +=1
             elif num < 0 :
                 negative_v += 1
        return[positive_v,negative_v]

#Time Complexity- O(N)
#Space Complexity- O(1)
