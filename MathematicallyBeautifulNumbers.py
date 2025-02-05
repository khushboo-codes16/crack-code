def is_mathematically_beautiful(x, k):
    seen_powers = set()
    current_power = 1

    while x > 0:
        remainder = x % k
        
        # If remainder is greater than 1, the number cannot be beautiful
        if remainder > 1:
            return "NO"
        
        # Move to the next division level
        x //= k
        
    return "YES"

# Read input
T = int(input())

for _ in range(T):
    x, k = map(int, input().split())
    print(is_mathematically_beautiful(x, k))
