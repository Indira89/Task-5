input_string = input()
def most_frequent_character(input_string):
    # Create a dictionary to store character frequencies
    char_freq = {}

    # Count the frequency of each character
    for char in input_string:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1

    # Find the character with the maximum frequency
    most_frequent_char = max(char_freq, key=char_freq.get)

    return most_frequent_char
print(most_frequent_character)