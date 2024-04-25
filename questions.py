# 23. Given two strings, string1 and string2, determine if there exists a one to one character mapping between each character of string1 to string2.
# Example:

# string1 = 'qwe'
# string2 = 'asd'
# string_map(string1, string2) == True
# # q = a, w = s, and e = d

def string_map(string1, string2):
    # Check if the lengths of both strings are the same
    if len(string1) != len(string2):
        return False

    # Create dictionaries to store mappings from string1 to string2 and vice versa
    map1_to_2 = {}
    map2_to_1 = {}

    # Iterate over each character in both strings
    for char1, char2 in zip(string1, string2):
        # Check if there's already a mapping for char1 to char2 or vice versa
        if char1 in map1_to_2:
            if map1_to_2[char1] != char2:
                return False
        if char2 in map2_to_1:
            if map2_to_1[char2] != char1:
                return False
        # Add mappings
        map1_to_2[char1] = char2
        map2_to_1[char2] = char1

    # If all characters are mapped one-to-one, return True
    return True


# Example usage
string1 = 'qwe'
string2 = 'asd'
print(string_map(string1, string2))  # Output: True


################################################################################################
