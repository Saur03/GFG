'''
Program to find Smallest and Largest Word in a String
Given a string, find the minimum and the maximum length words in it. 

Examples: 
Input : "This is a test string"
Output : Minimum length word: a
         Maximum length word: string
Input : "GeeksforGeeks A computer Science portal for Geeks"
Output : Minimum length word: A
         Maximum length word: GeeksforGeeks
'''
import re

# Function to find the smallest and largest words in a string using regular expressions
def find_smallest_largest_words_regex(input_str):
    # Define a regular expression pattern to match words
    word_regex = r'\b\w+\b'
    words = re.findall(word_regex, input_str)

    # Initialize variables to store the smallest and largest words
    smallest_word = ""
    largest_word = ""

    # Iterate through the words in the string
    for word in words:
        # Check if the current word is smaller than the smallest word found so far
        if len(word) < len(smallest_word) or not smallest_word:
            smallest_word = word

        # Check if the current word is larger than the largest word found so far
        if len(word) > len(largest_word):
            largest_word = word

    # Print the smallest and largest words
    print("Minimum length word:", smallest_word)
    print("Maximum length word:", largest_word)

# Input string
input_str = "This is a test string"

# Call the function to find and display the smallest and largest words
find_smallest_largest_words_regex(input_str)

