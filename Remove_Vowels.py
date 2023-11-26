string = "Guvi Geeks Network Private Limited"
vowels = "aeiouAEIOU"

def remove_vowels(string):
    result = ""
    for char in string:
        if char not in vowels:
            result += char

    return result

new_string = remove_vowels(string)
print(new_string)