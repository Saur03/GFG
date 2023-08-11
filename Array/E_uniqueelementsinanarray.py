'''
Print all Distinct ( Unique ) Elements in given Array
Examples: 

Input: arr[] = {12, 10, 9, 45, 2, 10, 10, 45}
Output: 12, 10, 9, 45, 2

Input: arr[] = {1, 2, 3, 4, 5}
Output: 1, 2, 3, 4, 5
'''
def printDistinct(arr, n):
    for i in range(0, n):
        # Check if the picked element is already printed
        d = 0
        for j in range(0, i):
             if (arr[i] == arr[j]):
                 d = 1
                 break
        # If not printed earlier, then print it     
        if (d == 0):  
            print(arr[i])

arr = [6, 10, 5, 4, 9, 120, 4, 6, 10]
n = len(arr)
printDistinct(arr, n)
              