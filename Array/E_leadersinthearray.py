'''
Leaders in an array
For example:

Input: arr[] = {16, 17, 4, 3, 5, 2}, 
Output: 17, 5, 2

Input: arr[] = {1, 2, 3, 4, 5, 2}, 
Output: 5, 2
'''
def printLeaders(arr,size):
    for i in range(0, size):
        for j in range(i+1, size):
            if arr[i]<=arr[j]:
                break
        if j == size-1: # If loop didn't break
            print (arr[i],end=' ')
 
arr=[16, 17, 4, 3, 5, 2]
printLeaders(arr, len(arr))
 