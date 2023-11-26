string = "Guvi Geeks Network Private Limited"

def unique_characters(string):
    unique_set = set(string)
    unique_result = "".join(unique_set)
    return unique_result

# Example usage:
input_string = "abcaadef"
unique_string = unique_characters(string)

print("Original String:", string)
print("String with Unique Characters:", unique_string)