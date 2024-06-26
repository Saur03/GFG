'''
Find K most occurring elements in the given Array
Last Updated : 15 May, 2024
Given an array of N numbers and a positive integer K. 
The problem is to find K numbers with the most occurrences, i.e., the top K numbers having the maximum frequency. 
If two numbers have the same frequency then the number with a larger value should be given preference. 
The numbers should be displayed in decreasing order of their frequencies. 
It is assumed that the array consists of at least K numbers.

Examples: 

Input: arr[] = {3, 1, 4, 4, 5, 2, 6, 1}, K = 2
Output: 4 1
Explanation:
Frequency of 4 = 2, Frequency of 1 = 2
These two have the maximum frequency and 4 is larger than 1.

Input: arr[] = {7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9}, K = 4
Output: 5 11 7 10
Explanation: 
Frequency of 5 = 3, Frequency of 11 = 2, Frequency of 7 = 2, Frequency of 10 = 1
These four have the maximum frequency and 5 is largest among rest.
'''
# Python3 program to find k numbers with most
# occurrences in the given array

from collections import Counter

def print_N_mostFrequentNumber(nums, k, out):
    # Count the occurrences of each number
    counts = Counter(nums)

    # Get the k numbers with the highest occurrences
    most_frequent = counts.most_common(k)

    # Extract the numbers from the most frequent pairs
    numbers = [num for num, _ in most_frequent]

    # Store the numbers in the output list
    for i, num in enumerate(numbers):
        out[i] = num

    return out


# Driver's code
arr = [3, 1, 4, 4, 5, 2, 6, 1]
K = 2

# Function call
ans = [0] * K
print_N_mostFrequentNumber(arr, K, ans)
print(K, "numbers with most occurrences are:")
print(ans[::-1])
