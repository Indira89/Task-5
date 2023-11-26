string = "Guvi Geeks Network Private Limited"
def count_words(string):
    words = string.split()
    
    # Return the number of words
    return len(words)

word_count = count_words(string)

print(f"The number of words in the string is: {word_count}")
