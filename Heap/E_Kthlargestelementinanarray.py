'''
Given an array arr[] of size N, the task is to printing K largest elements in an array.
Note: Elements in output array can be in any order

Examples:
Input:  [1, 23, 12, 9, 30, 2, 50], K = 3
Output: 50, 30, 23

Input:  [11, 5, 12, 9, 44, 17, 2], K = 2
Output: 44, 17

K largest elements in an array using Sorting:
Sort the input array in descending order so that the first K elements in the array are the K largest elements

Follow the below steps to solve the problem:

Sort the elements in descending order
Print the first K numbers of the sorted array.
'''


def kLargest(arr, k):
    # Sort the given array arr in reverse
    # order.
    arr.sort(reverse=True)
    # Print the first kth largest elements
    for i in range(k):
        print(arr[i], end=" ")


# Driver code
arr = [1, 23, 12, 9, 30, 2, 50]
# n = len(arr)
k = 3
kLargest(arr, k)
