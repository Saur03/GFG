'''
Python program to interchange first and last elements in a list.
Given a list, write a Python program to swap first and last element of the list.

Examples: 

Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]

Input : [1, 2, 3]
Output : [3, 2, 1]
'''

# Approach1: Find the length of the list and simply swap the first element with (n-1)th element. 

# Swap function
def swapList(newList):
    size = len(newList)
     
    # Swapping 
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp
     
    return newList
     
# Driver code
newList = [12, 35, 9, 56, 24]
 
print(swapList(newList))