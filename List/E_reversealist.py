'''
Reversing a List in Python
Last Updated : 04 Dec, 2023
Python provides us with various ways of reversing a list. We will go through some of the many techniques on how a list in Python can be reversed.

Example: 

Input: list = [4, 5, 6, 7, 8, 9]
Output: [9, 8, 7, 6, 5, 4] 
Explanation: The list we are having in the output is reversed to the list we have in the input.
'''

'''
Reverse a List Using a Two-Pointer Approach
In this method, we will declare two pointers(basically the start index and the end index, 
let ‘left’ and ‘right’). While scanning the list, in each iteration we will swap the elements at index ‘left’ and ‘right’.

The ‘left’ pointer will move forward and the ‘right’ pointer will move backward. 
We will continue the process till ‘first’ < ‘last’. 
This will work for both an even number of elements as well an odd number of elements.
'''

# Reversing a list using two-pointer approach
def reverse_list(arr):
	left = 0
	right = len(arr)-1
	while (left < right):
		# Swap
		temp = arr[left]
		arr[left] = arr[right]
		arr[right] = temp
		left += 1
		right -= 1

	return arr

arr = [1, 2, 3, 4, 5, 6, 7]
print(reverse_list(arr))
