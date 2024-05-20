'''
In QuickSort, partition function is in-place, but we need extra space for recursive function calls. 
A simple implementation of QuickSort makes two calls to itself and in worst case requires O(n) space 
on function call stack. 

The worst case happens when the selected pivot always divides the array 
such that one part has 0 elements and other part has n-1 elements.
'''
# Python3 program for the above approach
def quickSort(arr, low, high):
	
	if (low < high):
	
		# pi is partitioning index, arr[p] is now
		# at right place
		pi = partition(arr, low, high)

		# Separately sort elements before
		# partition and after partition
		quickSort(arr, low, pi - 1)
		quickSort(arr, pi + 1, high)


