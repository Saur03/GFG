'''
URLify a given string (Replace spaces with %20)
Write a method to replace all the spaces in a string with ‘%20’. 
You may assume that the string has sufficient space at the end to hold the additional characters 
and that you are given the “true” length of the string.
Examples: 

Input: "Mr John Smith", 13
Output: Mr%20John%20Smith

Input: "Mr John Smith   ", 13
Output: Mr%20John%20Smith
'''
# Python3 implementation of above approach

# Instantiate the string
s = "Mr John Smith "

# Trim the given string
s = s.strip()

# Replace All space (unicode is \\s) to %20
s = s.replace(' ', "%20")

# Display the result
print(s) 

