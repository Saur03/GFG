'''
Minimum Number of Manipulations required to make two Strings Anagram Without Deletion of Character
Input : 
       s1 = "aba"
       s2 = "baa"
Output : 0
Explanation: Both String contains identical characters

Input :
       s1 = "ddcf"
       s2 = "cedk"
Output : 2
Explanation : Here, we need to change two characters
in either of the strings to make them identical. We 
can change 'd' and 'f' in s1 or 'e' and 'k' in s2.
'''
def min_anagram_manipulations(str1, str2):
    # Initialize a dictionary to store character frequencies
    char_freq = {}
    # Count character frequencies in the first string
    for char in str1:
        char_freq[char] = char_freq.get(char, 0) + 1
    # Count the differences in character frequencies using the second string
    diff_count = 0
    for char in str2:
        if char in char_freq and char_freq[char] > 0:
            char_freq[char] -= 1
        else:
            diff_count += 1
    # Calculate the total number of manipulations needed
    total_manipulations = sum(char_freq.values()) + diff_count
    return total_manipulations

str1 = "listen"
str2 = "silent"
result = min_anagram_manipulations(str1, str2)
print("Minimum manipulations:", result)                