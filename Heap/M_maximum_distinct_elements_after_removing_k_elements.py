'''
Maximum distinct elements after removing k elements
Given an array arr[] containing n elements. 
The problem is to find the maximum number of distinct elements (non-repeating) 
after removing k elements from the array. 
Note: 1 <= k <= n.
Examples: 

Input : arr[] = {5, 7, 5, 5, 1, 2, 2}, k = 3
Output : 4
Remove 2 occurrences of element 5 and
1 occurrence of element 2.

Input : arr[] = {1, 2, 3, 4, 5, 6, 7}, k = 5
Output : 2

Input : arr[] = {1, 2, 2, 2}, k = 1
Output : 1
'''
# Python3 code for the above approach

# function to return maximum number of distinct Toys
def MaxNumber(arr, N, K):

	# Count Number of distinct Number
	mp = {}
	for i in range(N):
		if arr[i] not in mp:
			mp[arr[i]] = 0
		mp[arr[i]] += 1
		
		# push them into vector
	v1 = []
	for i in mp:
		v1.append(mp[i])

	# add number of element except one element from every
	# distinct element
	temp = 0
	for i in range(len(v1)):
		temp += v1[i]-1
		
	# check if it is greater than simply return size of
	# vector otherwise decrement size of vector to fill k
	if K <= temp:
		return len(v1)
	else:
		K = K-temp
		ans = len(v1)
		while K:
			ans -= 1
			K -= 1
		return ans

# Driver Code
if __name__ == "__main__":

# Array
	arr = [10, 10, 10, 50, 50]
	K = 3
	
	# Size of array
	N = len(arr)
	print(MaxNumber(arr, N, K))

