import math

def calculate_rooms(test_cases):
    results = []
    for boys, girls, seats in test_cases:
        boys_rooms = math.ceil(boys / seats)
        girls_rooms = math.ceil(girls / seats)
        total_rooms = boys_rooms + girls_rooms
        results.append(total_rooms)
    return results

# Read input
t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

# Process and print output
for result in calculate_rooms(test_cases):
    print(result)
