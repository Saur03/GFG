'''
Maximum difference between two subsets of m elements
Given an array of n integers and a number m, find the maximum possible difference 
between two sets of m elements chosen from given array.

Examples: 
Input : arr[] = 1 2 3 4 5
            m = 4
Output : 4
The maximum four elements are 2, 3, 4 and 5. The minimum four elements are 1, 2, 3 and 4. The difference between
two sums is (2 + 3 + 4 + 5) - (1 + 2 + 3 + 4) = 4
  
Input : arr[] = 5 8 11 40 15 , m = 2
Output : 42
The difference is (40 + 15) - (5  + 8) 
'''
# Python program to find difference between max and min sum of array

def find_difference(arr, n, m):
	max = 0; min = 0
	
	# sort array 
	arr.sort();
	j = n-1
	for i in range(m):
		min += arr[i]
		max += arr[j]
		j = j - 1
	
	return (max - min)

# Driver code
if __name__ == "__main__":
	arr = [1, 2, 3, 4, 5]
	n = len(arr)
	m = 4

	print(find_difference(arr, n, m)) 

