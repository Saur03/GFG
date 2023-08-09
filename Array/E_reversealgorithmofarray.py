'''
Reversal algorithm for Array rotation
Examples: 

Input:  arr[] = {1, 2, 3, 4, 5, 6, 7}, d = 2
Output: 3, 4, 5, 6, 7, 1, 2
Explanation: If the array is rotated by 1 position to the left, 
it becomes {2, 3, 4, 5, 6, 7, 1}.
When it is rotated further by 1 position,
it becomes: {3, 4, 5, 6, 7, 1, 2}
'''

def reverseArray(arr, start, end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end = end-1
        
# Function to left rotate arr[] of size n by d

def leftRotate(arr, d):
    if d == 0:
         return
    n = len(arr)
     # in case the rotating factor is greater than array length
    d = d % n      
    reverseArray(arr, 0, d-1)   
    reverseArray(arr, d, n-1)
    reverseArray(arr, 0, n-1)
    
# Function to print an array
def printArray(arr):
      for i in range(0, len(arr)):
          print (arr[i],end=' ')
          
arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
d = 2
# Rotate array by 2
leftRotate(arr, d)
printArray(arr)              