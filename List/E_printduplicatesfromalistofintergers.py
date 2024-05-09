'''
Python | Program to print duplicates from a list of integers

Given a list of integers with duplicate elements in it. The task is to generate another list, which contains only the duplicate elements. In simple words, the new list should contain elements that appear as more than one.

Examples:

Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
Output : output_list = [20, 30, -20, 60]
Input :  list = [-1, 1, -1, 8]
Output : output_list = [-1]
'''
'''
Method 1: Using the Brute Force approach
'''
# Python program to print 
# duplicates from a list 
# of integers
def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated
 
# Driver Code
list1 = [10, 20, 30, 20, 20, 30, 40, 
         50, -20, 60, 60, -20, -20]
print (Repeat(list1))
