'''
An array is a type of data structure that stores elements of the same type in a contiguous block of memory. 
In an array, A, of size N, each memory location has some unique index,  (where 0 <i <N), that can be referenced as A[i].
Reverse an array of integers.

Example:-
A= [1,2,3]
Return = [3,2,1]
Function Description:- Complete the function reverseArray in the editor below.
reverseArray has the following parameter(s):
int A[n]: the array to reverse
Returns
int[n]: the reversed array
Input Format

The first line contains an integer, N, the number of integers in A .
The second line contains N space-separated integers that make up A .
'''

def reverseArray(a):
    n = len(a)
    for i in range(n//2):
        a[i], a[n-1 -i] = a[n-1-i], a[i]
    return a    


array = [1,2,3,4,5]
reverseArray(array)
print(array)

'''
TC: O(n)
SC: O(1)
'''

