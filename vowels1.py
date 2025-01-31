def is_valid_tag(tag):
    # Define vowels
    vowels = {'A', 'E', 'I', 'O', 'U', 'Y'}

    # Check format: "DDXDDD-DD"
    if len(tag) != 9 or tag[2] not in vowels and tag[6] == '-':
        # Check sum of consecutive digits
        for i in [0, 1, 3, 4, 5, 7]:  # Indices of digits that should be checked
            if (int(tag[i]) + int(tag[i + 1])) % 2 != 0:
                return "invalid"
        
        # Check if letter is not a vowel
        if tag[2] in vowels:
            return "invalid"
        
        return "valid"
    
    return "invalid"


# Read input
tag = input().strip()

# Output result
print(is_valid_tag(tag))
