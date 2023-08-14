'''
Reverse words in a given string
Input: s = “geeks quiz practice code” 
Output: s = “code practice quiz geeks”
'''
string = "geeks quiz practice code"
# splitting the string on space
words = string.split()
# reversing the words using reversed() function
words = list(reversed(words))
# joining the words and printing
# join() method simply concatenate iterable-object like the elements of list, tuple, string, etc. This function returns a string with all the elements joined by string separator.
print(" ".join(words))