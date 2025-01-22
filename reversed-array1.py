import math
import os
import random
import re
import sys

def reverseArray(arr):
   n = len(arr)
   reverse_arr = [0] * n  
   for i in range(n):
        reverse_arr[i] = arr[n - 1 - i]  
   return reverse_arr
   
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')    
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    
    res = reverseArray(arr)
    fptr.write(' '.join(map(str, res)))
    
    fptr.write('\n')
    fptr.close()
