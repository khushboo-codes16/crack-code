def sum_abs(n):
    
    return (3 ** n) - 1
T = int(input())
for _ in range(T):
    N = int(input())
    result = sum_abs(N)
    print(result)
