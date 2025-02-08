def count_supernatural_numbers(n):
    def find_numbers(curr_product, start_digit):
        if curr_product > n:  # Agar product n se bada ho, return
            return
        if curr_product == n:  # Agar product n ke barabar hai
            nonlocal count
            count += 1
            return
        
        # 2 se lekar 9 tak digits add karte raho
        for digit in range(start_digit, 10):
            if digit != 1:  # Agar digit 1 na ho
                find_numbers(curr_product * digit, digit)  # Recursively check karo
    
    count = 0
    find_numbers(1, 2)  # Initial product 1 se start hoga, aur digits 2-9 consider karenge
    return count

# Input lena
n = int(input())
print(count_supernatural_numbers(n))
