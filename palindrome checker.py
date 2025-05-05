# -*- coding: utf-8 -*-
"""
Created on Mon May  5 11:20:30 2025

@author: User
"""

def normalize_input(input_string):
    # Remove spaces and convert to lowercase
    normalized_string = input_string.replace(" ", "").lower()
    return normalized_string

def is_palindrome(normalized_string):
    # Compare the normalized string with its reverse
    return normalized_string == normalized_string[::-1]

def main():
    # Get input from the user
    user_input = input("Enter a word or sentence: ")

    # Normalize the input
    normalized_string = normalize_input(user_input)

    # Check if the normalized string is a palindrome
    if is_palindrome(normalized_string):
        print("Yes, it's a palindrome!")
    else:
        print("No, it's not a palindrome.")

if __name__ == "__main__":
    main()
