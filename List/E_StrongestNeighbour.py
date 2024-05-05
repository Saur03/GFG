'''
Python program to find the Strongest Neighbour
Examples:

Input: 1 2 2 3 4 5
Output: 2 2 3 4 5

Input: 5 5
Output: 5

Approach:
Read the input array i.e,arr1.
for i=1 to sizeofarray-1
find the max value between arr1[i] and arr1[i-1].
store the above value in another array i.e, arr2.
print the values of arr2.
'''

def maximumAdjacent(arr1, n):
   
    # array to store the max 
    # value between adjacent pairs
    arr2 = []  
     
    # iterate from 1 to n - 1
    for i in range(1, n):
       
        # find max value between 
        # adjacent  pairs gets 
        # stored in r
        r = max(arr1[i], arr1[i-1])
         
        # add element 
        arr2.append(r)
         
    # printing the elements
    for ele in arr2 :
        print(ele,end=" ")
 




