'''
K’th Non-repeating Character
Given a string str of length n (1 <= n <= 106) and a number k, 
the task is to find the kth non-repeating character in the string.

Examples: 

Input : str = geeksforgeeks, k = 3
Output : r
Explanation: First non-repeating character is f, second is o and third is r.

Input : str = geeksforgeeks, k = 2
Output : o
'''
# Python code of the above approach
def kth_non_repeating_char(string, k):
    # Create an empty dictionary to store 
    # the counts of each character in the string
    char_counts = {}

    # Loop through the string and store 
    # the counts of each character in the dictionary
    for char in string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    # Loop through the string and find the kth non-repeating character
    non_repeating_count = 0
    for char in string:
        if char_counts[char] == 1:
            non_repeating_count += 1
            if non_repeating_count == k:
                # When the count of non-repeating 
                # characters equals k, return the character
                return char

    # If there is no kth non-repeating character in the string, return None
    return None

# Main function
if __name__ == "__main__":
    string = "geeksforgeeks"
    k = 3

    result = kth_non_repeating_char(string, k)

    if result is None:
        print("There is no kth non-repeating character in the string.")
    else:
        print(f"The {k}th non-repeating character in the string is {result}.")

