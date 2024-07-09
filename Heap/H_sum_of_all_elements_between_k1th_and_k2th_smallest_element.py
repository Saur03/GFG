'''
Sum of all elements between k1’th and k2’th smallest elements
Given an array of integers and two numbers k1 and k2. 
Find the sum of all elements between given two k1’th and k2’th smallest elements of the array. 
It may be assumed that (1 <= k1 < k2 <= n) and all elements of array are distinct.

Examples : 
Input : arr[] = {20, 8, 22, 4, 12, 10, 14},  k1 = 3,  k2 = 6  
Output : 26          
         3rd smallest element is 10. 6th smallest element 
         is 20. Sum of all element between k1 & k2 is
         12 + 14 = 26

Input : arr[] = {10, 2, 50, 12, 48, 13}, k1 = 2, k2 = 6 
Output : 73 
'''
# Python program to find sum of all element between to K1'th and k2'th smallest elements in array

# Returns sum between two kth smallest element of array
def sumBetweenTwoKth(arr, n, k1, k2):

	# Sort the given array
	arr.sort()

	result = 0
	for i in range(k1, k2-1):
		result += arr[i] 
	return result

# Driver code
arr = [ 20, 8, 22, 4, 12, 10, 14 ] 
k1 = 3; k2 = 6
n = len(arr)
print(sumBetweenTwoKth(arr, n, k1, k2))


