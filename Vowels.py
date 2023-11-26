string = "Guvi Geeks Network Private Limited"
vowels = "aeiouAEIOU"
 
count = sum(string.count(vowel) for vowel in vowels)
print(count)

individual_counts = {vowel: string.count(vowel) for vowel in vowels}
print(individual_counts)