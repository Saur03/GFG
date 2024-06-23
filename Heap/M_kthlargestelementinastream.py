'''
K’th largest element in a stream
Given an infinite stream of integers, find the Kth largest element at any point of time.

Note: Here we have a stream instead of a whole array and we are allowed to store only K elements.

Examples: 
Input: stream[] = {10, 20, 11, 70, 50, 40, 100, 5, . . .}, K = 3
Output: {_,   _, 10, 11, 20, 40, 50,  50, . . .}

Input: stream[] = {2, 5, 1, 7, 9, . . .}, K = 2
Output: {_, 2, 2, 5, 7, . . .} 
'''
# Python program for the above approach 
import heapq

# min heap DS
min = []
k = 3

# function to get all kth number
def getAllKthNumber(arr):

	# list to store kth largest number
	list = []

	# one by one adding values to the min heap
	for val in arr:

		# if the heap size is less than k , we add to
		# the heap
		if len(min) < k:
			heapq.heappush(min, val)

		# otherwise ,
		# first we compare the current value with the
		# min heap TOP value

		# if TOP val > current element , no need to
		# remove TOP , bocause it will be the largest kth
		# element anyhow

		# else we need to update the kth largest element
		# by removing the top lowest element
		else:
			if val > min[0]:
				heapq.heappop(min)
				heapq.heappush(min, val)

		# if heap size >=k we add
		# kth largest element
		# otherwise -1
		if len(min) >= k:
			list.append(min[0])
		else:
			list.append(-1)
	return list

# Driver Code
arr = [1, 2, 3, 4, 5, 6]

# Function call
res = getAllKthNumber(arr)

for x in res:
	print("Kth largest element is", x)


