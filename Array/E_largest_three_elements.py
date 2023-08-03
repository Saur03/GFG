'''
Find the largest three distinct elements in an array

Given an array with all distinct elements, find the largest three elements. Expected time complexity is O(n) and extra space is O(1). 

Example 1:
Input: arr[] = {10, 4, 3, 50, 23, 90}
Output: 90, 50, 23
'''

import sys

def print3largest(arr, arr_size):
    
    if (arr_size < 3):
        print(" Invalid Input ")
        return
    
    third = first = second = -sys.maxsize
    
    for i in range(0, arr_size):
        if (arr[i] > first):
            third = second
            second = first
            first = arr[i]
        
        elif (arr[i] > second):
            third = second
            second = arr[i]
        
        elif (arr[i] > third):
            third = arr[i]
        
    print("Three largest elements are", first, second, third)

# main code
arr = [12, 13, 1, 10, 34, 1]
n = len(arr)
print3largest(arr, n)