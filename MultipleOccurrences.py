import sys

def sum_of_absolute_differences(arr):
    index_map = {}
    
    # Store first and last occurrence of each number
    for i, num in enumerate(arr):
        if num not in index_map:
            index_map[num] = [i, i]  # First and last occurrence initialized to i
        else:
            index_map[num][1] = i  # Update last occurrence
    
    # Compute sum of absolute differences
    total_sum = sum(abs(v[1] - v[0]) for v in index_map.values())
    
    return total_sum

# Read input
t = int(sys.stdin.readline().strip())  # Number of test cases

for _ in range(t):
    n = int(sys.stdin.readline().strip())  # Number of elements in array
    arr = list(map(int, sys.stdin.readline().strip().split()))  # Read array elements
    
    # Print output for each test case
    print(sum_of_absolute_differences(arr))

