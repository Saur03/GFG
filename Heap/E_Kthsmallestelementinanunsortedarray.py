'''
program to find K'th smallest element
Given an array arr[] of size N and a number K, where K is smaller than the size of the array. 
Find the K’th smallest element in the given array. Given that all array elements are distinct.

Examples:  
Input: arr[] = {7, 10, 4, 3, 20, 15}, K = 3 
Output: 7

Input: arr[] = {7, 10, 4, 3, 20, 15}, K = 4 
Output: 10 
'''
# Function to return K'th smallest element in a given array

def kthSmallest(arr, N, K):

    # Sort the given array
    arr.sort()

    # Return k'th element in the sorted array
    return arr[K-1]


# Driver code
if __name__ == '__main__':
    arr = [12, 3, 5, 7, 19]
    N = len(arr)
    K = 2

    # Function call
    print("K'th smallest element is", kthSmallest(arr, N, K))

