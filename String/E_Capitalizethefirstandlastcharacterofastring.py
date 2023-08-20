'''
Capitalize the first and last character of each word in a string
Input: Geeks for geeks
Output: GeekS FoR GeekS

Input: Geeksforgeeks is best
Output: GeeksforgeekS IS BesT
'''
def capitalize_first_last(string):
    words = string.split()  # Split the string into words
    result = []
    
    for word in words:
        if len(word) > 1:
            modified_word = word[0].upper() + word[1:-1] + word[-1].upper()
        else:
            modified_word = word.upper()  # If word has only one character
            
        result.append(modified_word)
            
    return ''.join(result)

input_string = " Geeks for geeks "
capitalized_string = capitalize_first_last(input_string)
print(capitalized_string)
            