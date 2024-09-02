'''
Sliding Window Maximum (Maximum of all subarrays of size K)
Given an array and an integer K, find the maximum for each and every contiguous subarray of size K.

Examples : 

Input: arr[] = {1, 2, 3, 1, 4, 5}, K = 3 
Output: 3 3 4 5
Explanation: Maximum of 1, 2, 3 is 3
                       Maximum of 2, 3, 1 is 3
                       Maximum of 3, 1, 4 is 4
                       Maximum of 1, 4, 5 is 5

Input: arr[] = {8, 5, 10, 7, 9, 4, 15, 12, 90, 13}, K = 4 
Output: 10 10 10 15 15 90 90          
Explanation: Maximum of first 4 elements is 10, similarly for next 4 
                       elements (i.e from index 1 to 4) is 10, So the sequence 
                       generated is 10 10 10 15 15 90 90

Input: arr[] = {20, 10, 30}, K = 1 
Output: 20 10 30
'''
# Python3 program for the above approach

# Method to find the maximum for each
# and every contiguous subarray
# of size K

def printMax(arr, N, K):
    max = 0

    for i in range(N - K + 1):
        max = arr[i]
        for j in range(1, K):
            if arr[i + j] > max:
                max = arr[i + j]
        print(str(max) + " ", end="")


# Driver's code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    N = len(arr)
    K = 3
    
    # Function call
    printMax(arr, N, K)

