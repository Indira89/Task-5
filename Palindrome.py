string=input()
def is_palindrome(s):
    return s == s[::-1]

result = is_palindrome(string)

if result:
    print("True")
else:
    print("False")