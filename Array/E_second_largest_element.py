'''
Find Second largest element in an array
Given an array of integers, our task is to write a program that efficiently finds the second-largest element present in the array. 

Example:

Input: arr[] = {12, 35, 1, 10, 34, 1}
Output: The second largest element is 34.
Explanation: The largest element of the 
array is 35 and the second 
largest element is 34

Input: arr[] = {10, 5, 10}
Output: The second largest element is 5.
Explanation: The largest element of 
the array is 10 and the second 
largest element is 5

Input: arr[] = {10, 10, 10}
Output: The second largest does not exist.
Explanation: Largest element of the array 
is 10 there is no second largest element
'''
def second_largest_arr(arr):
    # sort the array
    arr.sort()
    n = len(arr)
    # there should be atleast 2 elements
    if (n<2):
        print("Invalid input")
    # Start from second last element as the largest element is at last
    for i in range(n-2, -1, -1):
        # If the element is not equal to largest element
         if (arr[i] != arr[n-1]):
             print("The second largest element of the given array is ", arr[i])
             return
                 
    print("There is no second largest element in the given array")
    
arr = [12, 35, 1, 10, 34, 1]
print("The given array is ", str(arr))
second_largest_arr(arr)        