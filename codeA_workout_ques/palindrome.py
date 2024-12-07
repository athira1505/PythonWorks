# Check Palindrome
# Write a Python function named is_palindrome(string) that takes a string and
# returns True if it is a palindrome, and False otherwise.
# Function Signature: def is_palindrome(string: str) -> bool:
# Input: A string string.
# Output: A boolean value indicating whether the string is a palindrome.
# is_palindrome("racecar") # should return True

string=input("enter the string:")
def is_palindrome(string:str):
    return string==string[::-1]

print(is_palindrome(string))