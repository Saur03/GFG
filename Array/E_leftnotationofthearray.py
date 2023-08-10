'''
Print left rotation of array in O(n) time and O(1) space
Input : 
arr[] = {1, 3, 5, 7, 9}
k1 = 1
k2 = 3
k3 = 4
k4 = 6
Output : 
3 5 7 9 1
7 9 1 3 5
9 1 3 5 7
3 5 7 9 1
'''
def leftRotate(arr, n, k):
    # To get the starting point of rotated array
    mod = k % n
    # Prints the rotated array from start position
    for i in range(n):
        print((arr[(mod + i) % n]), end= " ")
        return
    
arr = [1, 3, 5, 7, 9]
n = len(arr)
k = 2
leftRotate(arr, n, k)
k = 3    
leftRotate(arr, n, k)
k = 4
leftRotate(arr, n, k)

