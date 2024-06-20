'''
Question:- Sort a nearly sorted (or K sorted) array.
Given an array of N elements, where each element is at most K away from its target position, 
devise an algorithm that sorts in O(N log K) time.

Examples: 

Input: arr[] = {6, 5, 3, 2, 8, 10, 9}, K = 3 
Output: arr[] = {2, 3, 5, 6, 8, 9, 10}

Input: arr[] = {10, 9, 8, 7, 4, 70, 60, 50}, k = 4
Output: arr[] = {4, 7, 8, 9, 10, 50, 60, 70}
'''
# Function to sort an array using
# insertion sort


def insertionSort(A, size):
	i, key, j = 0, 0, 0
	for i in range(size):
		key = A[i]
		j = i-1

		# Move elements of A[0..i-1], that are
		# greater than key, to one position
		# ahead of their current position.
		# This loop will run at most k times
		while j >= 0 and A[j] > key:
			A[j + 1] = A[j]
			j = j - 1
		A[j + 1] = key
