def reverseArray(arr):
    return arr[::-1]   

 
n = int(input())

 
arr = list(map(int, input().split()))

 
reversed_arr = reverseArray(arr)

 
print(*reversed_arr)
