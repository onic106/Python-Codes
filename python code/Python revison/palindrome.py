def is_palindrome(s):
    return s == s[::-1]

input_string = "RACECAR"
if is_palindrome(input_string):
    print("Yes")
else:
    print("No")
