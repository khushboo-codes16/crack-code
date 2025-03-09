def sum_abs(n):
    return 2 ** n  # Using the correct formula

T = int(input())  # Number of test cases
for _ in range(T):
    N = int(input())  # Number of moves
    result = sum_abs(N)
    print(result)
